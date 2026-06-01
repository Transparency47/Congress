# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2590?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2590
- Title: Fresh Start Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2590
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-12-17T12:03:16Z
- Update date including text: 2025-12-17T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2590",
    "number": "2590",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Fresh Start Act of 2025",
    "type": "S",
    "updateDate": "2025-12-17T12:03:16Z",
    "updateDateIncludingText": "2025-12-17T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:04:46Z",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "DE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2590is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2590\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Van Hollen (for himself and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program for States for purposes of modernizing criminal justice data infrastructure to facilitate automatic record expungement and sealing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fresh Start Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Terms defined in Omnibus Crime Control and Safe Streets Act of 1968**\nTerms defined in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ) shall have the meanings given those terms in that section.\n**(2) Other terms**\n**(A) Automatic**\nThe term automatic means, with regard to the expungement or sealing of a criminal record, that the expungement or sealing occurs without the State requiring any action from the eligible individual.\n**(B) Covered expungement law**\nThe term covered expungement law means a law of a State providing for the automatic expungement or sealing, subject to such requirements as the State may impose, of a criminal record of an individual.\n#### 3. Establishment of grant program\n##### (a) In general\nThe Attorney General may make not more than 1 grant under this Act to each eligible State.\n##### (b) Amount\nA grant described in subsection (a) shall be in an amount of not more than $5,000,000.\n##### (c) Eligibility\nA State shall be eligible for a grant under this Act if\u2014\n**(1)**\nthe State has in effect a covered expungement law;\n**(2)**\nthe covered expungement law of the State provides that expungement or sealing of a criminal record shall not be delayed by reason of a failure to pay a fee or fine; and\n**(3)**\nthe State submits an application to the Attorney General containing such information as the Attorney General may require, including, at a minimum\u2014\n**(A)**\ninformation identifying whether a system exists, as of the date of the application, for record expungement or sealing in the State;\n**(B)**\na description of how infrastructure created through grant funding will facilitate automatic record expungement or sealing for individuals eligible for record expungement or sealing; and\n**(C)**\nan identification of the anticipated number of individuals who would benefit from the implementation of automatic record expungement or sealing infrastructure.\n#### 4. Use of grant amounts\nA State shall use a grant received under section 3 to implement a covered expungement law in accordance with the following requirements:\n**(1)**\nThe State shall use not more than 10 percent of the grant for research or planning for criminal record data infrastructure improvements that will make criminal record expungement or sealing automatic.\n**(2)**\nThe State shall use any remaining amounts to implement criminal record data infrastructure improvements that will make criminal record expungement or sealing automatic.\n**(3)**\nThe portion of the costs of implementing the law provided by a grant under this section may not exceed 75 percent.\n#### 5. Reporting requirements\n##### (a) In general\nA State receiving a grant under section 3 shall report to the Attorney General, each year of the grant term, pursuant to guidelines established by the Attorney General, information regarding the following:\n**(1)**\nThe number of individuals eligible for automatic expungement or sealing under the covered expungement law of the State, disaggregated by race, ethnicity, and gender.\n**(2)**\nThe number of individuals whose records have been expunged or sealed annually since the enactment of the covered expungement law of the State, disaggregated by race, ethnicity, and gender.\n**(3)**\nThe number of individuals who have submitted an application for expungement or sealing under the covered expungement law of the State that is still pending, disaggregated by race, ethnicity, and gender.\n##### (b) Inaccessibility of data for reporting\nIf a State is unable to compile and report elements of the data on expungement and sealing required to be reported under subsection (a) during any year of the grant term, the State shall develop and report, not later than the last day of that year, a comprehensive plan to obtain as much of the unavailable data as possible.\n##### (c) Publication\nNot later than 1 year after the date of enactment of this Act, and each year thereafter, the Attorney General shall make available to the public a report containing the data reported to the Attorney General under this section.\n#### 6. Authorization of appropriations\nThere are authorized to be appropriated $50,000,000 for each of fiscal years 2026 through 2030 to carry out this Act.",
      "versionDate": "2025-07-31",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-18T19:19:17Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2590is.xml"
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
      "title": "Fresh Start Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fresh Start Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program for States for purposes of modernizing criminal justice data infrastructure to facilitate automatic record expungement and sealing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:34:02Z"
    }
  ]
}
```
