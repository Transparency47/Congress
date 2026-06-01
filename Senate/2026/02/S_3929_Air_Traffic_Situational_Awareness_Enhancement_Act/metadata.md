# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3929?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3929
- Title: Air Traffic Situational Awareness Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 3929
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-05-19T17:25:20Z
- Update date including text: 2026-05-19T17:25:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3929",
    "number": "3929",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Air Traffic Situational Awareness Enhancement Act",
    "type": "S",
    "updateDate": "2026-05-19T17:25:20Z",
    "updateDateIncludingText": "2026-05-19T17:25:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T16:24:21Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3929is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3929\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Sheehy (for himself, Mr. Merkley , Mr. Daines , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the Federal Aviation Administration to acquire and install certified airborne position reference tools at air traffic control towers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Air Traffic Situational Awareness Enhancement Act .\n#### 2. Improvements to air traffic situational awareness\n##### (a) Airborne position reference tool installation\nNot later than 1 year after the date of enactment of this section, the Administrator of the Federal Aviation Administration shall acquire and install certified Airborne Position Reference Tools at air traffic control towers of the Federal Aviation Administration that are\u2014\n**(1)**\noperating under contract with the Federal Aviation Administration pursuant to section 47124 of title 49, United States Code; and\n**(2)**\nnot equipped with Standard Terminal Automation Replacement Systems or other situational awareness tools.\n##### (b) Standard Terminal Automation Replacement System installation and maintenance\nSection 47124(f)(2) of title 49, United States Code, is amended to read as follows:\n(2) Installation and maintenance For any tower operated under the Contract Tower Program that is not equipped with Standard Terminal Automation Replacement Systems or other situational awareness tools as of the date of enactment of the Air Traffic Situational Awareness Enhancement Act , not later than 1 year after such date, the Secretary shall purchase a Standard Terminal Automation Replacement System, or any equivalent system, and install and maintain such system using services directly from an original equipment manufacturer or services of the Federal Aviation Administration. .\n##### (c) Standard Terminal Automation Replacement System funding\nSection 47124(f)(3) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B), by inserting and after the semicolon; and\n**(2)**\nby striking subparagraphs (C) through (E) and inserting the following:\n(C) shall establish, in consultation with contract tower operators, an appropriate training program to periodically train air traffic controllers employed by such operators to ensure proper and efficient integration and use of the situational awareness equipment and technology described in paragraph (1) into contract tower operations. .\n##### (d) Retroactivity\nNotwithstanding any other provision of law, the Secretary of Transportation shall provide to any airport sponsor or air traffic control tower described in subsection (a)\u2014\n**(1)**\nreimbursement for any certified situational awareness system (including Airborne Position Reference Tools in accordance with subsection (a)) that was independently acquired and installed prior to the date on which the Administrator installs any such system under subsection (a); or\n**(2)**\nreimbursement or retroactive grant funding in accordance with section 47124(b) of title 49, United States Code, for any certified situational awareness system (including a Standard Terminal Automation Replacement System) that was independently acquired and installed prior to the effective date of the amendments made by subsection (b).\n##### (e) Authorized expenditures for air navigation facilities and equipment\nSection 48101(c) of title 49, United States Code, is amended by adding at the end the following new paragraph:\n(10) The acquisition, installation, and annual operating expenses of certified Airborne Position Reference Tools at air traffic control towers that are operating under contract with the Federal Aviation Administration under section 47124 and are not equipped with Standard Terminal Automation Replacement Systems or other situational awareness tools. .",
      "versionDate": "2026-02-26",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "8597",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Air Traffic Situational Awareness Enhancement Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-19T14:47:31Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3929is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Air Traffic Situational Awareness Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "title": "Air Traffic Situational Awareness Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Federal Aviation Administration to acquire and install certified airborne position reference tools at air traffic control towers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T03:48:28Z"
    }
  ]
}
```
