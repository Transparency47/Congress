# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3724
- Title: Improving Reporting to Prevent Hate Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3724
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-26T18:27:00Z
- Update date including text: 2026-02-26T18:27:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3724",
    "number": "3724",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Improving Reporting to Prevent Hate Act of 2026",
    "type": "S",
    "updateDate": "2026-02-26T18:27:00Z",
    "updateDateIncludingText": "2026-02-26T18:27:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T16:59:03Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3724is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3724\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Ms. Hirono (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain reporting to the uniform crime reporting program.\n#### 1. Short title\nThis Act may be cited as the Improving Reporting to Prevent Hate Act of 2026 .\n#### 2. Requirement to credibly report hate crimes\nSection 505 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10156 ) is amended by adding at the end the following:\n(j) Requirement to credibly report hate crimes (1) Evaluation for reporting on hate crimes Not later than 3 years after the date of enactment of the Improving Reporting to Prevent Hate Act of 2026 , using the data acquired by the Attorney General in accordance with the Hate Crimes Statistics Act ( 34 U.S.C. 41305 ), the Attorney General shall establish a method of evaluating, and thereafter shall use the method to evaluate, whether a covered jurisdiction is credibly reporting hate crimes, including whether, for each year, a covered jurisdiction\u2014 (A) has not reported hate crime data to the Federal Bureau of Investigation; or (B) has reported zero hate crime incidents to the Federal Bureau of Investigation. (2) Eligibility (A) In general A covered jurisdiction that is found, through an evaluation under paragraph (1), not to have credibly reported hate crimes for a year shall not be eligible for an allocation under this section for the fiscal year beginning after that year. (B) Exception Subparagraph (A) shall not apply to a covered jurisdiction that is found, through an evaluation under paragraph (1), not to have credibly reported hate crimes for a year if the Attorney General certifies that the covered jurisdiction has conducted significant community public education and awareness initiatives on hate crimes. (3) Annual report Each year, the Attorney General shall publish on the internet website of the Department of Justice a report on the covered jurisdictions certified under paragraph (2)(B). (4) Definitions For purposes of this subsection: (A) Covered jurisdiction The term covered jurisdiction means a unit of local government that has requested a grant under this subpart and has a population of more than 100,000 people. (B) Has conducted significant community public education and awareness initiatives on hate crimes The term has conducted significant community public education and awareness initiatives on hate crimes , with respect to a covered jurisdiction, means the covered jurisdiction\u2014 (i) has\u2014 (I) made substantial progress towards comprehensive reporting of hate crimes; (II) adopted a policy on identifying, investigating, and reporting hate crimes; and (III) developed a standardized system of collecting and analyzing hate crimes and reporting hate crimes to the National Incident-Based Reporting System of the Federal Bureau of Investigation; or (ii) has\u2014 (I) established a unit or liaison specialized in identifying, investigating, and reporting hate crimes and engaging in community relations functions related to preventing hate crimes; or (II) conducted regular public meetings or educational forums on the impact of hate crimes, services available to victims of hate crimes, and any relevant Federal, State, or local laws related to hate crimes. (C) Hate crime The term hate crime means\u2014 (i) an act described in section 1(b)(1) of the Hate Crime Statistics Act ( 34 U.S.C. 41305(b)(1) ); and (ii) an act in violation of section 241, 245, 247, or 249 of title 18, United States Code. .",
      "versionDate": "2026-01-29",
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
        "updateDate": "2026-02-26T18:27:00Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3724is.xml"
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
      "title": "Improving Reporting to Prevent Hate Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Reporting to Prevent Hate Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to include certain reporting to the uniform crime reporting program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:29Z"
    }
  ]
}
```
