# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1018
- Title: INSTRUCT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1018
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1018",
    "number": "1018",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001233",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Messmer, Mark [R-IN-8]",
        "lastName": "Messmer",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "INSTRUCT Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-05T15:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1018ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1018\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Messmer introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require additional information in disclosures of foreign gifts and contracts from foreign sources.\n#### 1. Short title\nThis Act may be cited as the Instructing Noteworthy Steps toward Transparency to Rout and Undo Calamitous Transactions Act of 2025 or the INSTRUCT Act of 2025 .\n#### 2. Interagency information sharing\n##### (a) Public records and sharing of reports\nSection 117(e) of the Higher Education Act of 1965 ( 20 U.S.C. 1011f(e) ) is amended to read as follows:\n(e) (1) Public inspection All disclosure reports required by this section shall be public records open to inspection and copying during business hours. (2) Interagency information sharing Not later than 30 days after receiving a disclosure report from an institution in compliance with this section, the Secretary shall transmit an unredacted copy of such report (that includes the name and address of a foreign source disclosed in such report) to the Director of the Federal Bureau of Investigation, the Director of National Intelligence, the Director of the Central Intelligence Agency, the Secretary of State, the Secretary of Defense, the Attorney General, the Secretary of Commerce, the Secretary of Homeland Security, the Secretary of Energy, the Director of the National Science Foundation, and the Director of the National Institutes of Health. .\n##### (b) Interagency information sharing\nNot later than 90 days after the date of enactment of this Act, the Secretary of Education shall transmit to each individual listed in section 117(e)(2) of the Higher Education Act of 1965, as amended by this Act\u2014\n**(1)**\nany report received by the Department of Education under section 117 of the Higher Education Act of 1965 ( 20 U.S.C. 1011f ) prior to the date of enactment of this Act; and\n**(2)**\nany report, document, or other record generated by the Department of Education in the course of an investigation\u2014\n**(A)**\nof an institution with respect to the compliance of such institution with such section; and\n**(B)**\ninitiated prior to the date of enactment of this Act.\n##### (c) GAO Study and Report\n**(1) Study**\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall initiate a study to identify ways to improve intergovernmental agency coordination regarding implementation and enforcement of sections 117 of the Higher Education Act of 1965 ( 20 U.S.C. 1011f ), as amended by this Act, including increasing information sharing, increasing compliance rates, and establishing processes for enforcement.\n**(2) Report**\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress, and make public, a report containing the results of the study described in paragraph (1) .",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-31",
        "text": "Received in the Senate and Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1048",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DETERRENT Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-14T17:45:52Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-14T17:46:12Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-14T17:46:06Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-14T17:45:58Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-14T17:45:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-10T13:50:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "House",
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
          "measure-id": "id119hr1018",
          "measure-number": "1018",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1018v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Instructing Noteworthy Steps toward Transparency to Rout and Undo Calamitous Transactions Act of 2025 or the INSTRUCT Act of 2025</strong></p><p>This bill requires the Department of Education (ED) to share foreign gift and contract reports from institutions of higher education (IHEs) with specified federal agencies.</p><p>Under current law, an IHE must disclose to ED a gift from or contract with a foreign source that is valued at $250,000 or more, considered alone or in combination with all other gifts from or contracts with that foreign source. This bill requires ED, within 30 days of receiving a disclosure report from an\u00a0IHE, to transmit an\u00a0unredacted copy of the report to 11 listed agencies (e.g., the Federal Bureau of Investigation, the Department of State, and the Department of Homeland Security).</p><p>The bill also requires ED, within 90 days of the bill's enactment, to transmit additional information to these federal agencies. Specifically, ED must transmit (1) any disclosure report received by ED prior to the bill's enactment; and (2) any report, document, or other record generated by ED in the course of investigating an IHE's compliance with disclosure requirements\u00a0(and such investigation was initiated prior to the bill's enactment).\u00a0</p><p>The Government Accountability Office must study and report on ways to improve intergovernmental agency coordination for implementing and enforcing disclosure reporting requirements.</p>"
        },
        "title": "INSTRUCT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1018.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Instructing Noteworthy Steps toward Transparency to Rout and Undo Calamitous Transactions Act of 2025 or the INSTRUCT Act of 2025</strong></p><p>This bill requires the Department of Education (ED) to share foreign gift and contract reports from institutions of higher education (IHEs) with specified federal agencies.</p><p>Under current law, an IHE must disclose to ED a gift from or contract with a foreign source that is valued at $250,000 or more, considered alone or in combination with all other gifts from or contracts with that foreign source. This bill requires ED, within 30 days of receiving a disclosure report from an\u00a0IHE, to transmit an\u00a0unredacted copy of the report to 11 listed agencies (e.g., the Federal Bureau of Investigation, the Department of State, and the Department of Homeland Security).</p><p>The bill also requires ED, within 90 days of the bill's enactment, to transmit additional information to these federal agencies. Specifically, ED must transmit (1) any disclosure report received by ED prior to the bill's enactment; and (2) any report, document, or other record generated by ED in the course of investigating an IHE's compliance with disclosure requirements\u00a0(and such investigation was initiated prior to the bill's enactment).\u00a0</p><p>The Government Accountability Office must study and report on ways to improve intergovernmental agency coordination for implementing and enforcing disclosure reporting requirements.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1018"
    },
    "title": "INSTRUCT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Instructing Noteworthy Steps toward Transparency to Rout and Undo Calamitous Transactions Act of 2025 or the INSTRUCT Act of 2025</strong></p><p>This bill requires the Department of Education (ED) to share foreign gift and contract reports from institutions of higher education (IHEs) with specified federal agencies.</p><p>Under current law, an IHE must disclose to ED a gift from or contract with a foreign source that is valued at $250,000 or more, considered alone or in combination with all other gifts from or contracts with that foreign source. This bill requires ED, within 30 days of receiving a disclosure report from an\u00a0IHE, to transmit an\u00a0unredacted copy of the report to 11 listed agencies (e.g., the Federal Bureau of Investigation, the Department of State, and the Department of Homeland Security).</p><p>The bill also requires ED, within 90 days of the bill's enactment, to transmit additional information to these federal agencies. Specifically, ED must transmit (1) any disclosure report received by ED prior to the bill's enactment; and (2) any report, document, or other record generated by ED in the course of investigating an IHE's compliance with disclosure requirements\u00a0(and such investigation was initiated prior to the bill's enactment).\u00a0</p><p>The Government Accountability Office must study and report on ways to improve intergovernmental agency coordination for implementing and enforcing disclosure reporting requirements.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1018"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1018ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "INSTRUCT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T02:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "INSTRUCT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Instructing Noteworthy Steps toward Transparency to Rout and Undo Calamitous Transactions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require additional information in disclosures of foreign gifts and contracts from foreign sources.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:21Z"
    }
  ]
}
```
