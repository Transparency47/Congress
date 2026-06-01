# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1007?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1007
- Title: 9–8–8 Lifeline Cybersecurity Responsibility Act
- Congress: 119
- Bill type: S
- Bill number: 1007
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-06T06:32:44Z
- Update date including text: 2025-12-06T06:32:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1007",
    "number": "1007",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
    "type": "S",
    "updateDate": "2025-12-06T06:32:44Z",
    "updateDateIncludingText": "2025-12-06T06:32:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T21:50:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1007is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1007\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Mullin (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title V of the Public Health Service Act to secure the suicide prevention lifeline from cybersecurity incidents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 9\u20138\u20138 Lifeline Cybersecurity Responsibility Act .\n#### 2. Protecting suicide prevention lifeline from cybersecurity incidents\n##### (a) National suicide prevention lifeline program\nSection 520E\u20133(b) of the Public Health Service Act (42 U.S.C. 290bb\u201336c(b)) is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) coordinating with the Chief Information Security Officer of the Department of Health and Human Services to take such steps as may be necessary to ensure the program is protected from cybersecurity incidents and eliminates known cybersecurity vulnerabilities. .\n##### (b) Reporting\nSection 520E\u20133 of the Public Health Service Act ( 42 U.S.C. 290bb\u201336c ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Cybersecurity reporting (1) In general (A) In general The program\u2019s network administrator receiving Federal funding pursuant to subsection (a) shall report to the Assistant Secretary, in a manner that protects personal privacy, consistent with applicable Federal and State privacy laws\u2014 (i) any identified cybersecurity vulnerabilities to the program within 24 hours of identification of such a vulnerability; and (ii) any identified cybersecurity incidents to the program within 24 hours of identification of such incident. (B) Local and regional crisis centers Local and regional crisis centers participating in the program shall report to the program\u2019s network administrator described in subparagraph (A), in a manner that protects personal privacy, consistent with applicable Federal and State privacy laws\u2014 (i) any identified cybersecurity vulnerabilities to the program within 24 hours of identification of such vulnerability; and (ii) any identified cybersecurity incidents to the program within 24 hours of identification of such incident. (2) Notification If the program\u2019s network administrator receiving funding pursuant to subsection (a) discovers, or is informed by a local or regional crisis center pursuant to paragraph (1)(B) of, a cybersecurity vulnerability or incident described in such paragraph, within 24 hours of such discovery or receipt of information, such entity shall report the vulnerability or incident to the Assistant Secretary. (3) Clarification (A) Oversight (i) Local and regional crisis center Except as provided in clause (ii), local and regional crisis centers participating in the program shall oversee all technology each center employs in the provision of services as a participant in the program. (ii) Network administrator The program\u2019s network administrator receiving Federal funding pursuant to subsection (a) shall oversee the technology each crisis center employs in the provision of services as a participant in the program if such oversight responsibilities are established in the applicable network participation agreement. (B) Supplement, not supplant The cybersecurity incident reporting requirements under this subsection shall supplement, and not supplant, cybersecurity incident reporting requirements under other provisions of applicable Federal law that are in effect on the date of the enactment of the 9\u20138\u20138 Lifeline Cybersecurity Responsibility Act . .\n##### (c) Study\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct and complete a study that evaluates cybersecurity risks and vulnerabilities associated with the 9\u20138\u20138 National Suicide Prevention Lifeline; and\n**(2)**\nsubmit a report of the findings of such study to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "912",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-04-11T14:29:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T14:29:42Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-04-11T14:29:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T14:29:42Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-11T14:29:42Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-11T14:29:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-31T15:34:06Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1007is.xml"
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
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "9\u20138\u20138 Lifeline Cybersecurity Responsibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title V of the Public Health Service Act to secure the suicide prevention lifeline from cybersecurity incidents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:38Z"
    }
  ]
}
```
