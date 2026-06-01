# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4104
- Title: Corporate Crime Database Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4104
- Origin chamber: Senate
- Introduced date: 2026-03-16
- Update date: 2026-04-01T18:05:22Z
- Update date including text: 2026-04-01T18:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in Senate
- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1057)
- Latest action: 2026-03-16: Introduced in Senate

## Actions

- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1057)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4104",
    "number": "4104",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Corporate Crime Database Act of 2026",
    "type": "S",
    "updateDate": "2026-04-01T18:05:22Z",
    "updateDateIncludingText": "2026-04-01T18:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S1057)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T21:01:14Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4104is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4104\nIN THE SENATE OF THE UNITED STATES\nMarch 16, 2026 Mr. Durbin (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Director of the Bureau of Justice Statistics to establish a database with respect to corporate offenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Corporate Crime Database Act of 2026 .\n#### 2. Corporate crime database at the Bureau of Justice Statistics\n##### (a) In general\nPart C of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10131 et seq. ) is amended by adding at the end the following:\n305. Corporate crime database (a) Definitions In this section: (1) Business entity The term business entity means a corporation, association, partnership, limited liability company, limited liability partnership, or other legal entity. (2) Corporate offense The term corporate offense means\u2014 (A) a violation or alleged violation of Federal law committed by\u2014 (i) a business entity; or (ii) an individual employed by a business entity within the conduct of the individual's occupational role; and (B) any other violation determined by the Director to be a corporate offense. (3) Director The term Director means the Director of the Bureau. (4) Enforcement action The term enforcement action includes any concluded administrative, civil, or criminal enforcement action or any declination, settlement, deferred prosecution agreement, or non-prosecution agreement entered into by a Federal agency to enforce a law or regulation. (5) Federal agency The term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code. (b) Establishment Beginning not later than 1 year after the date of enactment of the Corporate Crime Database Act of 2026 , the Director shall\u2014 (1) collect, aggregate, and analyze information regarding enforcement actions taken with respect to corporate offenses; and (2) publish on the internet website of the Bureau a database of the enforcement actions described in paragraph (1). (c) Information included The database established under subsection (b) shall include the following information on an enforcement action with respect to corporate offenses: (1) Each business entity or individual identified by the enforcement action. (2) The employer of an individual identified under paragraph (1), as determined relevant by the Director. (3) The parent company of a business entity identified under paragraph (1) or the parent company of any employer identified under paragraph (2), as determined relevant by the Director. (4) The type of offense or alleged offense committed by the business entity or individual. (5) Any relevant statute or regulation violated by the business entity or individual. (6) Each Federal agency bringing the enforcement action. (7) The outcome of the enforcement action, if any, including all documentation relevant to the outcome. (8) A unique identifier for each business entity, individual, employer, or parent company identified by the enforcement action. (9) Any additional information the Director determines necessary to carry out the purposes of this section. (d) Information collection by Director (1) In general Not later than 180 days after the date of enactment of the Corporate Crime Database Act of 2026 , the Director shall establish guidance for the collection of information from each Federal agency that carries out an enforcement action with respect to corporate offenses, including identification of each Federal agency that shall submit information to the Director and the manner in which, time at which, and frequency with which the information shall be submitted. (2) Cooperation by Federal agencies Each Federal agency identified in the guidance established under paragraph (1) shall submit to the Director the information specified by the Director, in accordance with that guidance. (3) Timing of information included To the extent to which information is available, the database established under subsection (b) shall include the information described in subsection (c) on each enforcement action with respect to corporate offenses taken by a Federal agency before, on, or after the date of enactment of the Corporate Crime Database Act of 2026 . (e) Publication details (1) In general Not later than 1 year after the date of enactment of the Corporate Crime Database Act of 2026 , the Director shall publish on the internet website of the Bureau the database established under subsection (b) in a format that is searchable, downloadable, and accessible to the public. (2) Update of information The Director shall update the information included in the database established under subsection (b) each time the information is collected under subsection (d). (f) Report required Not later than 1 year after the publication of the database established under subsection (b), and annually thereafter, the Director shall submit to Congress a report including\u2014 (1) a description of the data collected and analyzed under this section related to corporate offenses, including an analysis of recidivism, offenses and alleged offenses, and enforcement actions; (2) an estimate of the impact of corporate offenses on victims and the public; and (3) recommendations, developed in consultation with the Attorney General, for legislative or administrative actions to improve the ability of Federal agencies to monitor, respond to, and deter instances of corporate offenses. .\n##### (b) Chief Data Officer Council\nSection 3520A(b) of title 44, United States Code, is amended\u2014\n**(1)**\nin paragraph (4), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) identify ways in which a Federal agency (as defined in section 305 of title I of the Omnibus Crime Control and Safe Streets Act of 1968) that carries out an enforcement action (as defined in that section) with respect to a corporate offense (as defined in that section) can improve the collection, digitalization, tabulation, sharing, and publishing of information under that section, and the standardization of those processes, in order to carry out that section. .",
      "versionDate": "2026-03-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4724",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Corporate Crime Database Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-04-01T18:05:22Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4104is.xml"
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
      "title": "Corporate Crime Database Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Corporate Crime Database Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Director of the Bureau of Justice Statistics to establish a database with respect to corporate offenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:18:34Z"
    }
  ]
}
```
