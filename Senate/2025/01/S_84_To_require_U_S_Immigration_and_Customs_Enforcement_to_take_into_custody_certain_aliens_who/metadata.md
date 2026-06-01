# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/84?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/84
- Title: Sarah's Law
- Congress: 119
- Bill type: S
- Bill number: 84
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/84",
    "number": "84",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Sarah's Law",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-14",
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
        "item": {
          "date": "2025-01-14T17:58:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "IA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "OK"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "ND"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "KS"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "LA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "NE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "KS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "ID"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "NE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "SD"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "WV"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "LA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "OK"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MS"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MO"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "MS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s84is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 84\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Ms. Ernst (for herself, Mr. Grassley , Mrs. Britt , Mr. Lankford , Mr. Cramer , Mr. Hagerty , Mr. Scott of South Carolina , Mr. Cruz , Mr. Budd , Mr. Crapo , Mr. Daines , Mr. Cornyn , Mr. Moran , Mr. Cassidy , Mr. Graham , Mrs. Fischer , Mr. Marshall , Mr. Sheehy , Mr. Risch , Mr. Curtis , Mr. Scott of Florida , Mr. Ricketts , Mr. Rounds , Mrs. Capito , Mr. Kennedy , Mr. Mullin , Mrs. Hyde-Smith , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require U.S. Immigration and Customs Enforcement to take into custody certain aliens who have been charged in the United States with a crime that resulted in the death or serious bodily injury of another person, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Sarah's Law .\n#### 2. Mandatory detention of certain aliens charged with a crime resulting in death or serious bodily injury\nSection 236(c) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by striking the comma at the end and inserting a semicolon;\n**(B)**\nin subparagraph (B), by striking the comma at the end and inserting a semicolon;\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nby striking sentence and inserting sentenced ; and\n**(ii)**\nby striking , or and inserting a semicolon;\n**(D)**\nin subparagraph (D), by striking the comma at the end and inserting ; or ; and\n**(E)**\nby inserting after subparagraph (D) the following:\n(E) (i) (I) was not inspected and admitted into the United States; (II) held a nonimmigrant visa (or other documentation authorizing admission into the United States as a nonimmigrant) that has been revoked under section 221(i); or (III) is described in section 237(a)(1)(C)(i); and (ii) has been charged by a prosecuting authority in the United States with any crime that resulted in the death or serious bodily injury (as defined in section 1365(h)(3) of title 18, United States Code) of another person, ; and\n**(2)**\nby adding at the end the following:\n(3) Notification requirement Upon encountering or gaining knowledge of an alien described in paragraph (1), the Assistant Secretary of Homeland Security for Immigration and Customs Enforcement shall make reasonable efforts\u2014 (A) to obtain information from law enforcement agencies and from other available sources regarding the identity of any victims of the crimes for which such alien was charged or convicted; and (B) to provide the victim or, if the victim is deceased, a parent, guardian, spouse, or closest living relative of such victim, with information, on a timely and ongoing basis, including\u2014 (i) the alien\u2019s full name, aliases, date of birth, and country of nationality; (ii) the alien\u2019s immigration status and criminal history; (iii) the alien\u2019s custody status and any changes related to the alien\u2019s custody; and (iv) a description of any efforts by the United States Government to remove the alien from the United States. .\n#### 3. Savings provision\nNothing in this Act, or the amendments made by this Act, may be construed to limit the rights of crime victims under any other provision of law, including section 3771 of title 18, United States Code.",
      "versionDate": "2025-01-14",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-13T13:33:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119s84",
          "measure-number": "84",
          "measure-type": "s",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s84v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sarah's Law</strong></p> <p>This bill requires U.S. Immigration and Customs Enforcement (ICE) to detain a non-U.S. national (<i>alien</i> under federal law) who is unlawfully present in the United States and has been charged with a crime that resulted in the death or serious bodily injury of another person.</p> <p> ICE must make reasonable efforts to obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. ICE shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>"
        },
        "title": "Sarah's Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s84.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sarah's Law</strong></p> <p>This bill requires U.S. Immigration and Customs Enforcement (ICE) to detain a non-U.S. national (<i>alien</i> under federal law) who is unlawfully present in the United States and has been charged with a crime that resulted in the death or serious bodily injury of another person.</p> <p> ICE must make reasonable efforts to obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. ICE shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s84"
    },
    "title": "Sarah's Law"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sarah's Law</strong></p> <p>This bill requires U.S. Immigration and Customs Enforcement (ICE) to detain a non-U.S. national (<i>alien</i> under federal law) who is unlawfully present in the United States and has been charged with a crime that resulted in the death or serious bodily injury of another person.</p> <p> ICE must make reasonable efforts to obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. ICE shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s84"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s84is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Sarah's Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sarah's Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require U.S. Immigration and Customs Enforcement to take into custody certain aliens who have been charged in the United States with a crime that resulted in the death or serious bodily injury of another person, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:34Z"
    }
  ]
}
```
