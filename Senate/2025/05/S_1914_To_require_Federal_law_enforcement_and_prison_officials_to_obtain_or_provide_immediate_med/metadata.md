# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1914?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1914
- Title: Andrew Kearse Accountability for Denial of Medical Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1914
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T21:43:16Z
- Update date including text: 2025-12-05T21:43:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1914",
    "number": "1914",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Andrew Kearse Accountability for Denial of Medical Care Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:43:16Z",
    "updateDateIncludingText": "2025-12-05T21:43:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:53:38Z",
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
      "sponsorshipDate": "2025-05-22",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1914is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1914\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Ms. Warren (for herself, Mr. Blumenthal , Ms. Hirono , Mr. Markey , Mr. Merkley , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require Federal law enforcement and prison officials to obtain or provide immediate medical attention to individuals in custody who display medical distress.\n#### 1. Short title\nThis Act may be cited as the Andrew Kearse Accountability for Denial of Medical Care Act of 2025 .\n#### 2. Medical attention for individuals in Federal custody displaying medical distress\n##### (a) In general\nChapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Medical attention for individuals in Federal custody displaying medical distress (a) Definitions In this section\u2014 (1) the term appropriate Inspector General , with respect to a covered official, means\u2014 (A) the Inspector General of the Federal agency that employs the covered official; or (B) in the case of a covered official employed by a Federal agency that does not have an Inspector General, the Inspector General of the Department of Justice; (2) the term covered official means\u2014 (A) a Federal law enforcement officer (as defined in section 115); (B) an officer or employee of the Bureau of Prisons; or (C) an officer or employee of the United States Marshals Service; and (3) the term medical distress includes breathing difficulties. (b) Requirement (1) Offense It shall be unlawful for a covered official to negligently fail to obtain or provide immediate medical attention to an individual in Federal custody who displays medical distress in the presence of the covered official if the individual suffers unnecessary pain, injury, or death as a result of that failure. (2) Penalty A covered official who violates paragraph (1) shall be fined under this title, imprisoned for not more than 1 year, or both. (3) State civil enforcement Whenever an attorney general of a State has reasonable cause to believe that a resident of the State has been aggrieved by a violation of paragraph (1) by a covered official, the attorney general or another official, agency, or entity designated by the State may bring a civil action in any appropriate district court of the United States to obtain appropriate equitable and declaratory relief. (c) Inspector General investigation (1) In general The appropriate Inspector General shall investigate any instance in which\u2014 (A) a covered official fails to obtain or provide immediate medical attention to an individual in Federal custody who displays medical distress in the presence of the covered official; and (B) the individual suffers unnecessary pain, injury, or death as a result of the failure to obtain or provide immediate medical attention. (2) Referral for prosecution If an appropriate Inspector General, in conducting an investigation under paragraph (1), concludes that a covered official acted negligently in failing to obtain or provide immediate medical attention to an individual in Federal custody, the appropriate Inspector General shall refer the case to the Attorney General for prosecution under this section. (3) Confidential complaint process The Inspector General of a Federal agency that employs covered officials shall establish a process under which an individual may confidentially submit a complaint to the Inspector General regarding an incident described in paragraph (1) involving a covered official employed by the Federal agency (or, in the case of the Inspector General of the Department of Justice, involving a covered official employed by a Federal agency that does not have an Inspector General). (d) Training The head of an agency that employs covered officials shall provide training to each covered official on obtaining or providing medical assistance to individuals in medical distress. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Medical attention for individuals in Federal custody displaying medical distress. .",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3603",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Andrew Kearse Accountability for Denial of Medical Care Act of 2025",
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
        "updateDate": "2025-06-13T13:44:44Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1914is.xml"
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
      "title": "Andrew Kearse Accountability for Denial of Medical Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Andrew Kearse Accountability for Denial of Medical Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Federal law enforcement and prison officials to obtain or provide immediate medical attention to individuals in custody who display medical distress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:23Z"
    }
  ]
}
```
