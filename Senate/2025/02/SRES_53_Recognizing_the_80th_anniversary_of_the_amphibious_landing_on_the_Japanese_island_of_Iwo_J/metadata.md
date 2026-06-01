# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/53?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/53
- Title: A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.
- Congress: 119
- Bill type: SRES
- Bill number: 53
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-03-24T19:54:47Z
- Update date including text: 2025-03-24T19:54:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-02-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-02-19 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1037; text: 2/4/2025 CR S597-598)
- 2025-02-19 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-02-19 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-02-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-02-19 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1037; text: 2/4/2025 CR S597-598)
- 2025-02-19 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-02-19 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/53",
    "number": "53",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
    "type": "SRES",
    "updateDate": "2025-03-24T19:54:47Z",
    "updateDateIncludingText": "2025-03-24T19:54:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1037; text: 2/4/2025 CR S597-598)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-02-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
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
            "date": "2025-02-19T23:21:14Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-02-04T19:32:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MO"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "ND"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AL"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "NC"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "KS"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "MS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "NE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "AZ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "WV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "NH"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres53is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 53\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Young (for himself, Mr. Warner , Mr. Blumenthal , Mr. Sullivan , Mr. Coons , Mr. Boozman , Ms. Cortez Masto , Mr. Cramer , Mr. Gallego , Mr. Cruz , Mr. Kaine , Ms. Ernst , Mr. King , Mr. Scott of Florida , Ms. Klobuchar , Mr. Tillis , Ms. Rosen , Mr. Reed , Mr. Van Hollen , Mr. Banks , and Ms. Warren ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nRecognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.\nThat the Senate\u2014\n**(1)**\nrecognizes the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima that began on February 19, 1945, and ended on March 26, 1945;\n**(2)**\ncommemorates the iconic and historic raisings of the flag of the United States on Mount Suribachi that occurred on February 23, 1945;\n**(3)**\nhonors the Marines, Sailors, Soldiers, Army Air Crew, and Coast Guardsmen who fought bravely on Iwo Jima, including the thousands of Japanese soldiers who tenaciously defended the island;\n**(4)**\nremembers and venerates the service members who gave their last full measure of devotion on the battlefield;\n**(5)**\nrecognizes the Allied victory at the Battle of Iwo Jima, which\u2014\n**(A)**\nwas led by the United States Marine Corps; and\n**(B)**\nmade the defeat of the Empire of Japan in World War II possible;\n**(6)**\naffirms the immortal words of Admiral Chester Nimitz, who stated that uncommon valor was a common virtue among the service members of the United States who fought on Iwo Jima;\n**(7)**\nreaffirms the bonds of friendship and shared values between the United States and Japan, whose strong and resilient alliance demonstrates the power of reconciliation between former adversaries;\n**(8)**\nencourages the people of the United States to honor the veterans of the Battle of Iwo Jima with appropriate programs, ceremonies, and activities;\n**(9)**\nhonors the service and sacrifice of the men and women who serve the United States today, carrying on the proud tradition of the individuals who came before them; and\n**(10)**\nsalutes the 250th year since the founding of the United States Marine Corps and the United States Navy.",
      "versionDate": "2025-02-04",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres53ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 53\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Young (for himself, Mr. Warner , Mr. Blumenthal , Mr. Sullivan , Mr. Coons , Mr. Boozman , Ms. Cortez Masto , Mr. Cramer , Mr. Gallego , Mr. Cruz , Mr. Kaine , Ms. Ernst , Mr. King , Mr. Scott of Florida , Ms. Klobuchar , Mr. Tillis , Ms. Rosen , Mr. Reed , Mr. Van Hollen , Mr. Banks , Ms. Warren , Mr. Schmitt , Mrs. Fischer , Mr. Cotton , Ms. Duckworth , Mr. Justice , Mr. Rounds , Mr. Schiff , Mr. Hoeven , Mr. Tuberville , Mr. Daines , Mr. Budd , Mr. Moran , Mr. Wicker , Mr. Ricketts , Mr. Kelly , Mrs. Capito , Mrs. Shaheen , and Mrs. Blackburn ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nFebruary 19, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.\nThat the Senate\u2014\n**(1)**\nrecognizes the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima that began on February 19, 1945, and ended on March 26, 1945;\n**(2)**\ncommemorates the iconic and historic raisings of the flag of the United States on Mount Suribachi that occurred on February 23, 1945;\n**(3)**\nhonors the Marines, Sailors, Soldiers, Army Air Crew, and Coast Guardsmen who fought bravely on Iwo Jima, including the thousands of Japanese soldiers who tenaciously defended the island;\n**(4)**\nremembers and venerates the service members who gave their last full measure of devotion on the battlefield;\n**(5)**\nrecognizes the Allied victory at the Battle of Iwo Jima, which\u2014\n**(A)**\nwas led by the United States Marine Corps; and\n**(B)**\nmade the defeat of the Empire of Japan in World War II possible;\n**(6)**\naffirms the immortal words of Admiral Chester Nimitz, who stated that uncommon valor was a common virtue among the service members of the United States who fought on Iwo Jima;\n**(7)**\nreaffirms the bonds of friendship and shared values between the United States and Japan, whose strong and resilient alliance demonstrates the power of reconciliation between former adversaries;\n**(8)**\nencourages the people of the United States to honor the veterans of the Battle of Iwo Jima with appropriate programs, ceremonies, and activities;\n**(9)**\nhonors the service and sacrifice of the men and women who serve the United States today, carrying on the proud tradition of the individuals who came before them; and\n**(10)**\nsalutes the 250th year since the founding of the United States Marine Corps and the United States Navy.",
      "versionDate": "2025-02-19",
      "versionType": "ATS"
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
            "name": "Asia",
            "updateDate": "2025-02-20T15:56:52Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-02-20T15:56:41Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-02-20T15:56:47Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-02-20T15:57:24Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2025-02-20T15:57:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:24:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres53",
          "measure-number": "53",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres53v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945. Additionally, the resolution recognizes the 250th year since the founding of the U.S. Marine Corps and the U.S. Navy.</p>"
        },
        "title": "A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres53.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945. Additionally, the resolution recognizes the 250th year since the founding of the U.S. Marine Corps and the U.S. Navy.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119sres53"
    },
    "title": "A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945. Additionally, the resolution recognizes the 250th year since the founding of the U.S. Marine Corps and the U.S. Navy.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119sres53"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres53is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres53ats.xml"
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
      "title": "A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:33:35Z"
    },
    {
      "title": "A resolution recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T11:56:20Z"
    }
  ]
}
```
