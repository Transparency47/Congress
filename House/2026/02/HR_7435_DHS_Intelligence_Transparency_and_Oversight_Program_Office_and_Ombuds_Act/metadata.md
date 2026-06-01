# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7435
- Title: DHS Intelligence Transparency and Oversight Program Office and Ombuds Act
- Congress: 119
- Bill type: HR
- Bill number: 7435
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-19T08:05:48Z
- Update date including text: 2026-05-19T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7435",
    "number": "7435",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "DHS Intelligence Transparency and Oversight Program Office and Ombuds Act",
    "type": "HR",
    "updateDate": "2026-05-19T08:05:48Z",
    "updateDateIncludingText": "2026-05-19T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-10T19:03:12Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7435ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7435\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Magaziner (for himself and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to establish an Intelligence Transparency and Oversight Program Office and Intelligence Ombuds within the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DHS Intelligence Transparency and Oversight Program Office and Ombuds Act .\n#### 2. Establishment of the transparency and oversight program office and intelligence ombuds\n##### (a) In general\nTitle VII of the Homeland Security Act of 2002 ( 6 U.S.C. 341 et seq. ) is amended by adding at the end the following new section:\n714. Intelligence transparency and oversight program office; Ombuds (a) Establishment (1) In general The Secretary shall establish within the Department an Intelligence Transparency and Oversight Program Office (in this section referred to as the Office ) to carry out the following: (A) Review and assess information concerning intelligence activities of the Department, including relating to the timeliness, objectivity, and independence from political considerations of such activities. (B) Facilitate departmental decisions regarding making information publicly available in a manner that enhances public understanding of such activities. (2) Ombuds The Office shall be headed by an Ombuds, who shall\u2014 (A) be a senior, career employee; (B) not hold any other position within the Department; (C) have a background in\u2014 (i) intelligence; (ii) civil rights enforcement; and (iii) addressing matters of intelligence timeliness, objectivity, and politicization; (D) report directly to the Under Secretary for Intelligence and Analysis; and (E) report directly to Congress with respect to any urgent concerns. (b) Duties of the Ombuds The Ombuds shall have the following duties: (1) Serve, in consultation with the Privacy Officer appointed under section 222 and the Officer for Civil Rights and Civil Liberties, as the Department\u2019s principal advisor regarding the following: (A) Safeguarding objectivity in intelligence activities of the Department. (B) Ensuring such activities are independent from political considerations. (2) Remain current and well-informed of issues affecting intelligence activities. (3) Promote awareness among intelligence components of the Department of the requirement that all intelligence activities of the Department shall be\u2014 (A) conducted in a manner consistent with the protection of privacy rights, civil rights, and civil liberties; and (B) objective and independent from political considerations. (4) Provide, without fear of retaliation, confidential forums to hear and help resolve individual and organizational concerns regarding intelligence activities of the Department, including relating to real or perceived occurrences of civil rights or civil liberties abuses, or politicization of analysis, biased reporting, or lack of objectivity in intelligence collection or analysis. (5) Initiate reviews and make recommendations to the heads of the intelligence components of the Department, as appropriate, related to the matters described in paragraph (4). (6) Facilitate departmental decisions regarding making information publicly available in a manner that enhances public understanding of the intelligence activities of the Department, while continuing to protect information when disclosure of such information would harm homeland security. (7) Ensure that the functions performed by the Ombuds are complementary to existing functions within the Department. (c) Coordination with intelligence components of the Department (1) In general The heads of the intelligence components of the Department shall each establish procedures to provide formal responses to recommendations submitted to such officials by the Ombuds pursuant to subsection (b)(5) within 60 days of receiving such recommendations. (2) Access to information The Secretary shall establish procedures to provide the Ombuds access to all departmental information necessary to execute the responsibilities of the Ombuds under this section. The Ombuds may submit to the Secretary a request for such information, and not later than 60 days after receiving such a request, the Secretary shall provide the Ombuds with such information. (d) Annual reports Not later than one year after the enactment of this Act and annually thereafter, the Ombuds shall submit to the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate a report on its activities, findings, and recommendations of the Ombuds over the immediately preceding 12-month period. (e) Definition In this section the term intelligence activity means the collection, gathering, processing, analysis, production, or dissemination of information, including homeland security information, terrorism information, and weapons of mass destruction information. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 713 the following new item:\nSec. 714. Intelligence transparency and oversight program office; Ombuds. .",
      "versionDate": "2026-02-09",
      "versionType": "Introduced in House"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-18T16:06:15Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7435ih.xml"
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
      "title": "DHS Intelligence Transparency and Oversight Program Office and Ombuds Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DHS Intelligence Transparency and Oversight Program Office and Ombuds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to establish an Intelligence Transparency and Oversight Program Office and Intelligence Ombuds within the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:33:44Z"
    }
  ]
}
```
