
import omdb


path_to_input_file = 'd:\My\Python\homework_from_Orest_Voloshchuk\hw02\movie_names2'
path_to_good_movies_file = ''
path_to_invalid_titles_file = ''
path_to_invalid_metascore_file = ''


def getMovieData(pathToFile):
    movieData = {}
    i=0
    with open(pathToFile) as inputFile:
        for line in inputFile:
            i=i+1
            print i,":  "+line
            dataItem = omdb.search(line.rstrip())
            movieData.update({line.rstrip():dataItem or ''})
    inputFile.close()
    return movieData


def getMovieScore(movieData):
    invalid_metascore = []
    good_movies = []
    for key, value in movieData.iteritems():
        if value == '':
            continue
        else:
            for movieMetaData in value:
                if movieMetaData['title'].encode('utf-8') == key and (movieMetaData['type'] == 'movie' or movieMetaData['type'] == 'series'):
                    imdb_metascore = omdb.imdbid(movieMetaData['imdb_id'])['metascore'] or ''
                    print "score: ", imdb_metascore
                    if imdb_metascore == 'N/A' or not imdb_metascore.isdigit():
                        invalid_metascore.append(key)
                    else:
                        good_movies.append({key, imdb_metascore})
                    break
    # print len(invalid_metascore)
    # print len(good_movies)
    return invalid_metascore, good_movies


def getInvalidTitles(movieData):
    list_of_invalid_titles = []
    for key, value in movieData.iteritems():
        if value == '':
            list_of_invalid_titles.append(key)
    return list_of_invalid_titles


if __name__ == '__main__':

    movieData = getMovieData(path_to_input_file)  # get dict of movie_title with metadata from input file
    invalid_titles = getInvalidTitles(movieData)
    invalid_metascore = getMovieScore(movieData)[0]
    good_movies = getMovieScore(movieData)[1]

    with open('invalid_metascore','w') as invalid_m:
        for item in invalid_metascore:
            invalid_m.write(item+'\n')
    invalid_m.close()

    with open('invalid_title','w') as invalid_t:
        for item in invalid_titles:
            invalid_t.write(item+'\n')
    invalid_t.close()

    with open('good_movies','w') as good_m:
        for k,v in good_movies:
            good_m.write("\""+k+",\" "+v +'\n')
    good_m.close()



