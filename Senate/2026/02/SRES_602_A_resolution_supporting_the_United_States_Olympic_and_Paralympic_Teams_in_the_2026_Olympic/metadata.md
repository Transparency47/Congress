# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/602
- Title: A resolution supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.
- Congress: 119
- Bill type: SRES
- Bill number: 602
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-03-03T19:54:54Z
- Update date including text: 2026-03-03T19:54:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S515)
- 2026-02-05 - IntroReferral: Submitted in Senate
- 2026-02-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2026-02-25 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2026-02-25 - Discharge: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-02-25 - Committee: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- Latest action: 2026-02-05: Submitted in Senate

## Actions

- 2026-02-05 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S515)
- 2026-02-05 - IntroReferral: Submitted in Senate
- 2026-02-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2026-02-25 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2026-02-25 - Discharge: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-02-25 - Committee: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/602",
    "number": "602",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.",
    "type": "SRES",
    "updateDate": "2026-03-03T19:54:54Z",
    "updateDateIncludingText": "2026-03-03T19:54:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S515)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4302 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4302 proposed by Senator Moreno for Senator Klobuchar. To modify the number of medals won by Team USA.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 4302 proposed by Senator Moreno for Senator Klobuchar.",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-02-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 4302 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "602",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-03"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-02-25",
          "links": {
            "link": {
              "name": "SA 4302",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4302"
            }
          },
          "text": "Amendment SA 4302 agreed to in Senate by Unanimous Consent."
        },
        "number": "4302",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "M001242",
              "firstName": "Bernie",
              "fullName": "Sen. Moreno, Bernie [R-OH]",
              "lastName": "Moreno",
              "party": "R",
              "state": "OH",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "M001242",
              "firstName": "Bernie",
              "fullName": "Sen. Moreno, Bernie [R-OH]",
              "lastName": "Moreno",
              "party": "R",
              "state": "OH",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2026-02-25T05:00:00Z",
        "purpose": "To modify the number of medals won by Team USA.",
        "sponsors": {
          "item": {
            "bioguideId": "K000367",
            "firstName": "Amy",
            "fullName": "Sen. Klobuchar, Amy [D-MN]",
            "lastName": "Klobuchar",
            "party": "D",
            "state": "MN"
          }
        },
        "submittedDate": "2026-02-25T05:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-02-26T12:08:20Z"
      }
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2026-02-25T23:06:01Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-02-05T19:52:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "OK"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AR"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "UT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "UT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "OK"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-05",
      "state": "ME"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WV"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "RI"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "SD"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NJ"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres602is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 602\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Ms. Klobuchar (for herself, Mr. Bennet , Mr. Lankford , Mr. Boozman , Mr. Hickenlooper , Mr. Lee , Mr. Schiff , Mr. Curtis , Mr. Padilla , Mr. Mullin , Mr. King , Mrs. Blackburn , Mrs. Gillibrand , Mr. Blumenthal , Mr. Barrasso , Mr. Kim , Mrs. Capito , Mr. Reed , Mr. Rounds , Ms. Slotkin , Mr. Justice , and Mr. Coons ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nSupporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.\nThat the Senate\u2014\n**(1)**\napplauds the athletes and coaches of the United States Olympic and Paralympic Teams (referred to in this resolution as Team USA ) and the families who support them;\n**(2)**\ncommends the Government of Italy and the regional and local governments of Italy, including the governments of Milan and Cortina d\u2019Ampezzo, for their efforts to commit tremendous resources to provide a safe and secure environment for the 2026 Olympic and Paralympic Games;\n**(3)**\nsupports the athletes of Team USA in competing at the 2026 Olympic and Paralympic Winter Games; and\n**(4)**\ncommits to ensuring a safe and secure environment for the fans attending and athletes competing in the 2028 Los Angeles Olympic and Paralympic Summer Games, at events in both Los Angeles and Oklahoma City, and in the 2034 Utah Olympic and Paralympic Winter Games.",
      "versionDate": "2026-02-05",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres602ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 602\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Ms. Klobuchar (for herself, Mr. Bennet , Mr. Lankford , Mr. Boozman , Mr. Hickenlooper , Mr. Lee , Mr. Schiff , Mr. Curtis , Mr. Padilla , Mr. Mullin , Mr. King , Mrs. Blackburn , Mrs. Gillibrand , Mr. Blumenthal , Mr. Barrasso , Mr. Kim , Mrs. Capito , Mr. Reed , Mr. Rounds , Ms. Slotkin , Mr. Justice , Mr. Coons , and Mr. Booker ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nFebruary 25, 2026 Committee discharged; considered and agreed to with an amended preamble\nRESOLUTION\nSupporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.\nThat the Senate\u2014\n**(1)**\napplauds the athletes and coaches of the United States Olympic and Paralympic Teams (referred to in this resolution as Team USA ) and the families who support them;\n**(2)**\ncommends the Government of Italy and the regional and local governments of Italy, including the governments of Milan and Cortina d\u2019Ampezzo, for their efforts to commit tremendous resources to provide a safe and secure environment for the 2026 Olympic and Paralympic Games;\n**(3)**\nsupports the athletes of Team USA in competing at the 2026 Olympic and Paralympic Winter Games; and\n**(4)**\ncommits to ensuring a safe and secure environment for the fans attending and athletes competing in the 2028 Los Angeles Olympic and Paralympic Summer Games, at events in both Los Angeles and Oklahoma City, and in the 2034 Utah Olympic and Paralympic Winter Games.",
      "versionDate": "2026-02-25",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-20",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1069",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Athletes",
            "updateDate": "2026-02-27T16:05:20Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-02-27T16:05:41Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2026-02-27T16:05:49Z"
          },
          {
            "name": "Olympic games",
            "updateDate": "2026-02-27T16:05:25Z"
          },
          {
            "name": "Sports and recreation facilities",
            "updateDate": "2026-02-27T16:06:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2026-02-10T00:30:02Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres602is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres602ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:26Z"
    },
    {
      "title": "A resolution supporting the United States Olympic and Paralympic Teams in the 2026 Olympic and Paralympic Winter Games.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T11:56:19Z"
    }
  ]
}
```
