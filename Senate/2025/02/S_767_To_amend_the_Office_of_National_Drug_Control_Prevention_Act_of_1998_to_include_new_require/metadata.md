# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/767
- Title: HIDTA Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 767
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-01-10T07:28:21Z
- Update date including text: 2026-01-10T07:28:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/767",
    "number": "767",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "HIDTA Enhancement Act",
    "type": "S",
    "updateDate": "2026-01-10T07:28:21Z",
    "updateDateIncludingText": "2026-01-10T07:28:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T16:22:15Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "AK"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s767is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 767\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Kelly (for himself, Mrs. Capito , Mrs. Blackburn , Ms. Cortez Masto , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Office of National Drug Control Prevention Act of 1998 to include new requirements for assessments and reports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HIDTA Enhancement Act .\n#### 2. Office of National Drug Control Policy\nThe Office of National Drug Control Policy Reauthorization Act of 1998 ( 21 U.S.C. 1701 et seq. ) is amended\u2014\n**(1)**\nin section 706(g)(3) ( 21 U.S.C. 1705(g)(3) )\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) a report describing the use of HIDTA funds to investigate organizations and individuals trafficking in fentanyl or fentanyl-related substances, including any resulting prosecution, in the prior calendar year, including\u2014 (i) the amounts of fentanyl or fentanyl-related substances seized by a HIDTA-funded initiative in the area during the previous year; and (ii) law enforcement and predictive data from regional HIDTA threat assessments showing patterns and trends in substance abuse, trafficking, and transportation of fentanyl and fentanyl-related substances. ;\n**(2)**\nin section 707 ( 21 U.S.C. 1706 )\u2014\n**(A)**\nin subsection (l)(2)\u2014\n**(i)**\nin subparagraph (F), by striking and at the end;\n**(ii)**\nin subparagraph (G), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(H) any limitations of the ability of a high intensity drug trafficking area to meet the purpose or goals of the area and recommendations to address any such limitations, including through resource allocation, partnerships, or a change in authority or law. ;\n**(B)**\nin subsection (p)\u2014\n**(i)**\nin paragraph (5), by striking and at the end;\n**(ii)**\nin paragraph (6), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(7) $333,000,000 for each of fiscal years 2025 through 2030. ;\n**(C)**\nin subsection (s)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking $10,000,000 and inserting $14,224,000 ;\n**(ii)**\nin paragraph (2), by striking and at the end;\n**(iii)**\nin paragraph (3), by striking the period at the end and inserting a semicolon; and\n**(iv)**\nby adding at the end the following:\n(4) providing assistance to Federal, State, local, and Tribal law enforcement agencies in investigations and activities related to the interdiction of fentanyl and other substances; and (5) any additional purpose the Director determines is appropriate to enhance fentanyl prevention, seizure, and interdiction activities. ; and\n**(D)**\nby adding at the end the following:\n(t) Additional prosecutorial resources (1) In general The Attorney General shall make available sufficient investigative and prosecution resources as may be practicable for the purposes described in this section, including temporary reassignment under subsection (b)(2) for fiscal years 2024 through 2030, during which such an assistant United States attorney shall prioritize the investigation and prosecution of organizations and individuals trafficking in fentanyl and fentanyl-related substances. Such temporary reassignment may be extended by the Attorney General for such time as may be necessary to conclude any ongoing investigation or prosecution in which the assistant United States attorney is engaged. (2) Process for temporary reassignment Not later than 180 days after the date of enactment of this subsection, the Attorney General shall establish a process under which the Director, in consultation with the Executive Boards of each designated high intensity drug trafficking area, may request an assistant United States attorney to be so temporarily reassigned in accordance with this subsection. .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2964",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fight Fentanyl Act",
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
        "updateDate": "2025-03-21T15:55:45Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s767is.xml"
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
      "title": "HIDTA Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HIDTA Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Office of National Drug Control Prevention Act of 1998 to include new requirements for assessments and reports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:22Z"
    }
  ]
}
```
