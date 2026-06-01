# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3546
- Title: Sunset Section 230 Act
- Congress: 119
- Bill type: S
- Bill number: 3546
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:05:26Z
- Update date including text: 2026-01-20T15:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3546",
    "number": "3546",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Sunset Section 230 Act",
    "type": "S",
    "updateDate": "2026-01-20T15:05:26Z",
    "updateDateIncludingText": "2026-01-20T15:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T21:51:10Z",
          "name": "Referred To"
        }
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "IA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3546is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3546\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Graham (for himself, Mr. Durbin , Mr. Grassley , Mr. Whitehouse , Mr. Hawley , Ms. Klobuchar , Mrs. Blackburn , Mr. Blumenthal , Mrs. Moody , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo repeal section 230 of the Communications Act of 1934.\n#### 1. Short title\nThis Act may be cited as the Sunset Section 230 Act .\n#### 2. Repeal of section 230\n##### (a) In general\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) is repealed.\n##### (b) Conforming amendments\n**(1) Communications Act of 1934**\nThe Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) is amended\u2014\n**(A)**\nin section 223(h) ( 47 U.S.C. 223(h) ), by striking paragraph (2) and inserting the following:\n(2) The term interactive computer service means any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically a service or system that provides access to the Internet and such systems operated or services offered by libraries or educational institutions. ; and\n**(B)**\nin section 231(b)(4) ( 47 U.S.C. 231(b)(4) ), by striking or section 230 .\n**(2) Trademark Act of 1946**\nSection 45 of the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 (commonly known as the Trademark Act of 1946 ) ( 15 U.S.C. 1127 ), is amended by striking the definition relating to the term Internet and inserting the following:\nThe term Internet means the international computer network of both Federal and non-Federal interoperable packet switched data networks. .\n**(3) Title 17, United States Code**\nSection 1401 of title 17, United States Code, is amended by striking subsection (g).\n**(4) Title 18, United States Code**\nPart I of title 18, United States Code, is amended\u2014\n**(A)**\nin section 1462, by striking (as defined in section 230(e)(2) of the Communications Act of 1934) each place the term appears and inserting (as defined in section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 )) ;\n**(B)**\nin section 1465, by striking (as defined in section 230(e)(2) of the Communications Act of 1934) and inserting (as defined in section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 )) ;\n**(C)**\nin section 2257(h)(2)(B)(v), by striking , except that deletion of a particular communication or material made by another person in a manner consistent with section 230(c) of the Communications Act of 1934 ( 47 U.S.C. 230(c) ) shall not constitute such selection or alteration of the content of the communication ; and\n**(D)**\nin section 2421A\u2014\n**(i)**\nin subsection (a), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as that term is defined in section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 )) ; and\n**(ii)**\nin subsection (b), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as that term is defined in section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 )) .\n**(5) Controlled Substances Act**\nSection 401(h)(3)(A)(iii)(II) of the Controlled Substances Act ( 21 U.S.C. 841(h)(3)(A)(iii)(II) ) is amended by striking , except that deletion of a particular communication or material made by another person in a manner consistent with section 230(c) of the Communications Act of 1934 shall not constitute such selection or alteration of the content of the communication .\n**(6) Webb-Kenyon Act**\nSection 3(b)(1) of the Act entitled An Act divesting intoxicating liquors of their interstate character in certain cases , approved March 1, 1913 (commonly known as the Webb-Kenyon Act ) ( 27 U.S.C. 122b(b)(1) ), is amended by striking (as defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting (as defined in section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 )) .\n**(7) Title 28, United States Code**\nSection 4102 of title 28, United States Code, is amended\u2014\n**(A)**\nby striking subsection (c); and\n**(B)**\nin subsection (e)\u2014\n**(i)**\nby striking construed to and all that follows through affect and inserting construed to affect ; and\n**(ii)**\nby striking defamation; or and all that follows and inserting defamation. .\n**(8) Daniel Anderl Judicial Security and Privacy Act of 2022**\nSection 5933(7) of the Daniel Anderl Judicial Security and Privacy Act of 2022 ( 28 U.S.C. 601 note prec.; Public Law 117\u2013263 ) is amended by striking section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) and inserting section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ) .\n**(9) Title 31, United States Code**\nSection 5362(6) of title 31, United States Code, is amended by striking section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting section 223 of the Communications Act of 1934 ( 47 U.S.C. 223 ) .\n**(10) National Telecommunications and Information Administration Organization Act**\nSection 157 of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 941 ) is amended\u2014\n**(A)**\nby striking subsection (e); and\n**(B)**\nby redesignating subsections (f) through (j) as subsections (e) through (i), respectively.\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-20T15:05:26Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3546is.xml"
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
      "title": "Sunset Section 230 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sunset Section 230 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal section 230 of the Communications Act of 1934.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:48:24Z"
    }
  ]
}
```
