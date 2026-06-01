# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/121
- Title: Recover Fraudulent COVID Funds Act
- Congress: 119
- Bill type: S
- Bill number: 121
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-01-09T12:03:22Z
- Update date including text: 2026-01-09T12:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/121",
    "number": "121",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Recover Fraudulent COVID Funds Act",
    "type": "S",
    "updateDate": "2026-01-09T12:03:22Z",
    "updateDateIncludingText": "2026-01-09T12:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T18:39:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T18:39:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DE"
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
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "LA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "UT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s121is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 121\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Lankford (for himself, Ms. Ernst , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo extend the statute of limitations for violations relating to pandemic-era programs to be 10 years.\n#### 1. Short title\nThis Act may be cited as the Recover Fraudulent COVID Funds Act .\n#### 2. Statute of limitations for violations relating to pandemic-era programs\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term pandemic-era law means\u2014\n**(A)**\nthe Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020 ( Public Law 116\u2013123 ; 134 Stat. 146);\n**(B)**\nthe Families First Coronavirus Response Act ( Public Law 116\u2013127 ; 134 Stat. 177);\n**(C)**\nthe CARES Act ( Public Law 116\u2013136 ; 134 Stat. 281);\n**(D)**\nthe Paycheck Protection Program and Health Care Enhancement Act ( Public Law 116\u2013139 ; 134 Stat. 620);\n**(E)**\ndivisions M and N of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ; 134 Stat. 1182);\n**(F)**\nthe American Rescue Plan Act of 2021 ( Public Law 117\u20132 ; 135 Stat. 4); or\n**(G)**\nan amendment made by a law described in subparagraphs (A) through (F); and\n**(2)**\nthe term pandemic-era program violation means an offense or other violation of law involving conduct that relates to or involves\u2014\n**(A)**\na program, project, or activity that was authorized or established by, or was carried out under, a pandemic-era law; or\n**(B)**\nfunding provided under a pandemic-era law.\n##### (b) Extension of statute of limitations\n**(1) Crimes**\nNo person shall be prosecuted, tried, or punished for any pandemic-era program violation that is a criminal offense unless the indictment is found or the information is instituted\u2014\n**(A)**\nnotwithstanding section 3282(a) of title 18, United States Code, within 10 years after such offense shall have been committed; or\n**(B)**\nwithin such longer period of years after such offense shall have been committed as is otherwise provided by law.\n**(2) Tariff Act of 1930**\nNotwithstanding section 621 of the Tariff Act of 1930 ( 19 U.S.C. 1621 ), no civil action, suit, or proceeding for the forfeiture of property accruing under the customs laws of the United States related to a pandemic-era program violation shall be instituted unless such civil action, suit, or proceeding is commenced within 10 years after the time when the alleged pandemic-era program violation was discovered, or within 3 years after the time when the involvement of the property in the alleged pandemic-era program violation was discovered, whichever was later, except that the time of the absence from the United States of the person whose property is subject to forfeiture, or of any concealment or absence of the property, shall not be reckoned within the 10-year period of limitation.\n**(3) False claims**\n**(A) In general**\nNotwithstanding section 3731(b)(1) of title 31, United States Code, a civil action under section 3730 of such title alleging a violation of section 3729 of such title that is a pandemic-era program violation may not be brought more than 10 years after the date on which the violation was committed.\n**(B) Notice**\nNotwithstanding section 3808 of title 31, United States Code, a notice to the person alleged to be liable with respect to a claim or statement that involves a pandemic-era violation shall be mailed or delivered in accordance with section 3803(d)(1) of such title not later than 10 years after the date on which the violation of section 3802 of such title is committed.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-13T16:00:30Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-13T16:00:11Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-13T16:00:25Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-03-13T16:22:41Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-13T16:00:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-20T19:24:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s121",
          "measure-number": "121",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s121v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Recover Fraudulent COVID Funds Act</strong></p><p>This bill extends the statute of limitations (i.e., time limit for bringing a legal action) to 10 years for criminal and civil\u00a0violations involving specified COVID-19 pandemic relief programs, such as violations involving fraudulent activity. Under current law, the statute of limitations is generally five years for violations concerning\u00a0these pandemic-era programs. The Paycheck Protection Program and the Economic\u00a0Injury Disaster Loan Program currently have 10-year statutes of limitations relating to program\u00a0fraud.</p><p></p>"
        },
        "title": "Recover Fraudulent COVID Funds Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s121.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Recover Fraudulent COVID Funds Act</strong></p><p>This bill extends the statute of limitations (i.e., time limit for bringing a legal action) to 10 years for criminal and civil\u00a0violations involving specified COVID-19 pandemic relief programs, such as violations involving fraudulent activity. Under current law, the statute of limitations is generally five years for violations concerning\u00a0these pandemic-era programs. The Paycheck Protection Program and the Economic\u00a0Injury Disaster Loan Program currently have 10-year statutes of limitations relating to program\u00a0fraud.</p><p></p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s121"
    },
    "title": "Recover Fraudulent COVID Funds Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Recover Fraudulent COVID Funds Act</strong></p><p>This bill extends the statute of limitations (i.e., time limit for bringing a legal action) to 10 years for criminal and civil\u00a0violations involving specified COVID-19 pandemic relief programs, such as violations involving fraudulent activity. Under current law, the statute of limitations is generally five years for violations concerning\u00a0these pandemic-era programs. The Paycheck Protection Program and the Economic\u00a0Injury Disaster Loan Program currently have 10-year statutes of limitations relating to program\u00a0fraud.</p><p></p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s121"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s121is.xml"
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
      "title": "Recover Fraudulent COVID Funds Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recover Fraudulent COVID Funds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend the statute of limitations for violations relating to pandemic-era programs to be 10 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:21Z"
    }
  ]
}
```
