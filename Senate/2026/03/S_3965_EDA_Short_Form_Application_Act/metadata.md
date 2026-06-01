# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3965
- Title: EDA Short Form Application Act
- Congress: 119
- Bill type: S
- Bill number: 3965
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-03-23T15:48:22Z
- Update date including text: 2026-03-23T15:48:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (text: CR S764)
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (text: CR S764)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3965",
    "number": "3965",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "EDA Short Form Application Act",
    "type": "S",
    "updateDate": "2026-03-23T15:48:22Z",
    "updateDateIncludingText": "2026-03-23T15:48:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works. (text: CR S764)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T15:52:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CO"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NV"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "WY"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "KS"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3965is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3965\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Barrasso (for himself, Mr. Kelly , Ms. Alsobrooks , Mr. Bennet , Ms. Cortez Masto , Mr. Daines , Mr. Fetterman , Mr. Hawley , Ms. Klobuchar , Ms. Lummis , Mr. Moran , Mr. Ossoff , Mr. Schatz , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the establishment and use of short form applications for rural communities applying for economic development grant programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the EDA Short Form Application Act .\n#### 2. Short form applications for rural communities in economic development programs\n##### (a) Definitions\nIn this section:\n**(1) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary of Commerce for Economic Development.\n**(2) Rural community**\nThe term rural community means an incorporated municipality, Tribal area, or territory\u2014\n**(A)**\nwith a population of not more than 10,000 individuals, as determined by the Bureau of the Census in the most recent decennial census; or\n**(B)**\nthat, as determined by the Assistant Secretary, is not located in a metropolitan statistical area, as designated by the Director of the Office of Management and Budget.\n##### (b) Short form applications\nNotwithstanding any other provision of law, the Assistant Secretary shall establish a short form application for rural communities that may be used by applicants in rural communities for any grant program administered by the Economic Development Administration.\n##### (c) Rural stakeholder input\nIn establishing a short form application under subsection (b), the Assistant Secretary shall solicit input from a representative group of stakeholders in rural communities on ways to improve the application process for grants from the Economic Development Administration, including\u2014\n**(1)**\nthe length of the applications;\n**(2)**\nthe information and documentation required or requested to be submitted as part of the applications;\n**(3)**\nthe possibility of standardizing base materials, such as budget templates, forms, and required attachments, across grant programs administered by the Economic Development Administration;\n**(4)**\nthe possibility of reducing repetitive sections of the applications that ask for information already provided to the Federal Government, such as information provided through SAM.gov, the Bureau of the Census, or a comprehensive economic development strategy (as defined in section 3 of the Public Works and Economic Development Act of 1965 (42 U.S.C. 3122));\n**(5)**\nthe degree of applicability to rural communities of questions in the applications and information and documentation described in paragraph (2); and\n**(6)**\nany other considerations the Assistant Secretary determines to be necessary for the establishment of the short form application.\n##### (d) Transparency\nIn carrying out this section, the Assistant Secretary shall make publicly available\u2014\n**(1)**\nsample successful applications, with personal and sensitive information redacted;\n**(2)**\ncriteria decision guides that explain how applications are reviewed and rated; and\n**(3)**\nstandardized guidance for rural communities to use in applying for grants from the Economic Development Administration.",
      "versionDate": "",
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
        "name": "Commerce",
        "updateDate": "2026-03-23T15:48:22Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3965is.xml"
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
      "title": "EDA Short Form Application Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EDA Short Form Application Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the establishment and use of short form applications for rural communities applying for economic development grant programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:41Z"
    }
  ]
}
```
