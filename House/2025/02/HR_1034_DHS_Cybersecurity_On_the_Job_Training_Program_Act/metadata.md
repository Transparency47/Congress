# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1034
- Title: DHS Cybersecurity On-the-Job Training Program Act
- Congress: 119
- Bill type: HR
- Bill number: 1034
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-11-21T12:04:41Z
- Update date including text: 2025-11-21T12:04:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-05 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- 2025-11-20 17:43:11 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Magaziner asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1034, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-05 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- 2025-11-20 17:43:11 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Magaziner asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1034, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1034",
    "number": "1034",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000489",
        "district": "18",
        "firstName": "Sylvester",
        "fullName": "Rep. Turner, Sylvester [D-TX-18]",
        "lastName": "Turner",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "DHS Cybersecurity On-the-Job Training Program Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:41Z",
    "updateDateIncludingText": "2025-11-21T12:04:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2025-11-20",
      "actionTime": "17:43:11",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Magaziner asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1034, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-05T18:14:21Z",
              "name": "Referred to"
            }
          },
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1034ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1034\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Turner of Texas (for himself and Mr. Luttrell ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to establish a DHS Cybersecurity On-the-Job Training Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DHS Cybersecurity On-the-Job Training Program Act .\n#### 2. DHS Cybersecurity On-the-Job Training Program\n##### (a) In general\nSubtitle A of title XXII of the Homeland Security Act of 2002 ( 6 U.S.C. 651 et seq. ) is amended by adding at the end the following new section:\n2220F. DHS Cybersecurity On-the-Job Training Program (a) In general There is established within the Agency a DHS Cybersecurity On-the-Job Training Program (in this section referred to as the Program ) to voluntarily train Department employees who are not currently in a cybersecurity position for work in matters relating to cybersecurity at the Department. The Program shall be led by the Director, in consultation with the Under Secretary for Management. (b) Duties of the Director In carrying out the Program under subsection (a), the Director\u2014 (1) shall develop a curriculum for the Program, incorporating existing curricula as appropriate and applicable, such as the Federal Cyber Defense Skilling Academy and other initiatives or successor programs, and consistent with the National Initiative for Cybersecurity Education Framework or any successor framework, which may include distance learning instruction, in-classroom instruction within a work location, on-the-job instruction under the supervision of experienced cybersecurity staff, or other means of training and education as determined appropriate by the Director; (2) shall develop criteria for participation in the Program and ensure cybersecurity personnel are appropriately coded to the National Initiative for Cybersecurity Education Framework and successor programs; (3) in accordance with the curriculum described in paragraph (1)\u2014 (A) shall make available cybersecurity training to employees of the Department; and (B) may, as appropriate, make available cybersecurity training to other Federal employees; and (4) shall, during the 7-year period beginning on the date of this enactment of this section, annually submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that includes\u2014 (A) information relating to the number of employees who participated in the Program in the preceding year; (B) an identification of the positions into which employees trained through the Program were hired after such training; (C) a description of metrics used to measure the success of the Program, which may include a skill inventory for applicable positions; (D) copies of the reports submitted pursuant to subsection (c)(1); and (E) any additional information relating to the duties specified in this subsection. (c) Duties of the Under Secretary for Management In carrying out the Program under subsection (a), the Under Secretary for Management shall\u2014 (1) during the 7-year period beginning on the date of the enactment of this section, submit to the Secretary an annual report on the status of vacancies in cybersecurity positions throughout the Department; (2) support efforts by the Director to identify and recruit individuals employed by the Department to participate in the Program; (3) implement policies, including continuing service agreements, to encourage participation in the Program by employees throughout the Department; and (4) conduct outreach to employees who complete the Program regarding cybersecurity job opportunities within the Department. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 ( Public Law 107\u2013296 ; 116 Stat. 2135) is amended by inserting after the item relating to section 2220E the following new item:\nSec. 2220F. DHS Cybersecurity On-the-Job Training Program. .",
      "versionDate": "2025-02-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-06-09T17:40:47Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-09T17:40:54Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-09T17:41:00Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-09T17:41:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T14:38:10Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1034ih.xml"
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
      "title": "DHS Cybersecurity On-the-Job Training Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DHS Cybersecurity On-the-Job Training Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to establish a DHS Cybersecurity On-the-Job Training Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T04:03:35Z"
    }
  ]
}
```
