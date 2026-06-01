# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1258
- Title: Improving Contractor Cybersecurity Act
- Congress: 119
- Bill type: HR
- Bill number: 1258
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-05-06T13:51:06Z
- Update date including text: 2025-05-06T13:51:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1258",
    "number": "1258",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Improving Contractor Cybersecurity Act",
    "type": "HR",
    "updateDate": "2025-05-06T13:51:06Z",
    "updateDateIncludingText": "2025-05-06T13:51:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1258ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1258\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Lieu introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 41, United States Code, to require information technology contractors to maintain a vulnerability disclosure policy and program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Contractor Cybersecurity Act .\n#### 2. Vulnerability disclosure policy and program required for information technology contractors\n##### (a) Amendment\nChapter 47 of division C of subtitle I of title 41, United States Code, is amended by adding at the end the following new section:\n4715. Vulnerability disclosure policy and program required (a) Requirements for information technology contractors The head of an executive agency may not enter into a contract for information technology unless the contractor maintains or does the following: (1) A vulnerability disclosure policy for information technology that\u2014 (A) includes\u2014 (i) a description of which systems are in scope; (ii) the type of information technology testing for each system that is allowed (or specifically not authorized); (iii) if a contractor includes systems that host sensitive information in the vulnerability disclosure policy, the contractor shall determine whether to impose restrictions on accessing, copying, transferring, storing, using, and retaining such information, including by\u2014 (I) prohibiting sensitive information from being saved, stored, transferred, or otherwise accessed after initial discovery; (II) directing that sensitive information be viewed only to the extent required to identify a vulnerability and that the information not be retained; or (III) limiting use of information obtained from interacting with the systems or services to be explored by the researcher to activities directly related to reporting security vulnerabilities; (iv) a description of how an individual may submit a vulnerability report that includes\u2014 (I) the location of where to send the report, such as a web form or email address; (II) a description of the type of information necessary to find and analyze the vulnerability (such as a description, the location, and potential impact of the vulnerability, the technical information needed to reproduce the vulnerability, and any proof of concept); and (III) a clear statement\u2014 (aa) that any individual that submits a vulnerability report may do so anonymously; and (bb) on how and whether any incomplete submission is evaluated; (v) a commitment from the contractor that the contractor will not pursue civil action for any accidental, good faith violation of the vulnerability disclosure policy; (vi) a commitment from the contractor that if an individual acting in accordance with the vulnerability disclosure policy of the contractor is sued by a third party, the contractor will inform the public or the court that the individual was acting in compliance with the vulnerability disclosure policy; (vii) a statement that describes the time frame in which the individual that submits a report, if known, will receive a notification of receipt of the report and a description of what steps will be taken by the contractor during the remediation process; and (viii) a set of guidelines that establishes what type of activity by a researcher are acceptable and unacceptable; and (B) does not\u2014 (i) require the submission of personally identifiable information of a researcher; and (ii) limit testing solely to entities approved by the contractor but rather authorizes the public to search for and report any vulnerability. (2) A description of additional procedures that describe how the contractor will communicate with the researcher, and how and when any communication occurs. (3) A description of the target timelines for and tracking of the following: (A) Notification of receipt to the individual that submits the report, if known. (B) An initial assessment, such as determining whether any disclosed vulnerability is valid. (C) Resolution of a vulnerability, including notification of the outcome to the researcher. (4) A page on the website of the contractor that\u2014 (A) allows for the submission of vulnerabilities by anyone relating to the information technology; (B) lists the contact information, such as a phone number or email address for an individual or team responsible for reviewing any such submission under subparagraph (A); and (C) describes the process by which a review is conducted, including how long it will take for the contractor to respond to the researcher and whether or not monetary rewards will be paid to the reporter for identifying a vulnerability. (5) In the case of a discovered vulnerability that the contractor is not responsible for patching, the contractor shall submit the vulnerability to the responsible party or direct the researcher to the appropriate party. (b) Reporting requirements and metrics Not later than 7 days after the date on which the vulnerability disclosure policy described in subsection (a) is published, and on an ongoing basis as vulnerability reports are received, an information technology contractor shall report to the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security the following information: (1) Any valid or credible report of a not previously known public vulnerability (including any misconfiguration) on a system that uses commercial software or services that affect or are likely to affect other parties in government or industry once a patch or viable mitigation is available. (2) Any other situation where the contractor determines it would be helpful or necessary to involve the Cybersecurity and Infrastructure Security Agency. (c) CISA submission of vulnerabilities The Cybersecurity and Infrastructure Security Agency shall communicate with and submit, as necessary, vulnerabilities to the MITRE Common Vulnerabilities and Exposures database and the National Institute of Standards and Technology National Vulnerability Database. (d) Definitions In this section: (1) Executive agency The term executive agency has the meaning given that term in section 133. (2) Researcher The term researcher means the individual who submits a vulnerability report. (3) Information technology The term information technology has the meaning given that term in section 11101 of title 40. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 47 of division C of subtitle I of title 41, United States Code, is amended by adding at the end the following new item:\n4715. Vulnerability disclosure policy and program required. .\n##### (c) Applicability\nThe amendments made by this section shall take effect on the date of the enactment of this section and shall apply to any contract entered into on or after such effective date.",
      "versionDate": "2025-02-12",
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
            "name": "Computers and information technology",
            "updateDate": "2025-05-02T15:11:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-02T15:12:04Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-05-02T15:11:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-03-31T14:44:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1258",
          "measure-number": "1258",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1258v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Contractor Cybersecurity Act</strong></p><p>This bill prohibits an executive agency from entering into a contract for information technology unless the contractor maintains a vulnerability disclosure policy (VDP) and program.</p><p>The contractor must report to the Cybersecurity and Infrastructure Security Agency (CISA) of the Department of Homeland Security, within seven days after the VDP is published\u00a0and on an ongoing basis as vulnerability reports are received, information regarding</p><ul><li>any valid or credible report of a not previously known public vulnerability on a system that uses commercial software or services that affect, or are likely to affect, other parties in government or industry once a patch or viable mitigation is available; and</li><li>any other situation where the contractor determines it would be helpful or necessary to involve CISA.</li></ul><p>CISA must submit vulnerabilities to the MITRE Common Vulnerabilities and Exposures database and the National Institute of Standards and Technology National Vulnerability Database.</p>"
        },
        "title": "Improving Contractor Cybersecurity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1258.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Contractor Cybersecurity Act</strong></p><p>This bill prohibits an executive agency from entering into a contract for information technology unless the contractor maintains a vulnerability disclosure policy (VDP) and program.</p><p>The contractor must report to the Cybersecurity and Infrastructure Security Agency (CISA) of the Department of Homeland Security, within seven days after the VDP is published\u00a0and on an ongoing basis as vulnerability reports are received, information regarding</p><ul><li>any valid or credible report of a not previously known public vulnerability on a system that uses commercial software or services that affect, or are likely to affect, other parties in government or industry once a patch or viable mitigation is available; and</li><li>any other situation where the contractor determines it would be helpful or necessary to involve CISA.</li></ul><p>CISA must submit vulnerabilities to the MITRE Common Vulnerabilities and Exposures database and the National Institute of Standards and Technology National Vulnerability Database.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1258"
    },
    "title": "Improving Contractor Cybersecurity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Contractor Cybersecurity Act</strong></p><p>This bill prohibits an executive agency from entering into a contract for information technology unless the contractor maintains a vulnerability disclosure policy (VDP) and program.</p><p>The contractor must report to the Cybersecurity and Infrastructure Security Agency (CISA) of the Department of Homeland Security, within seven days after the VDP is published\u00a0and on an ongoing basis as vulnerability reports are received, information regarding</p><ul><li>any valid or credible report of a not previously known public vulnerability on a system that uses commercial software or services that affect, or are likely to affect, other parties in government or industry once a patch or viable mitigation is available; and</li><li>any other situation where the contractor determines it would be helpful or necessary to involve CISA.</li></ul><p>CISA must submit vulnerabilities to the MITRE Common Vulnerabilities and Exposures database and the National Institute of Standards and Technology National Vulnerability Database.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1258"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1258ih.xml"
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
      "title": "Improving Contractor Cybersecurity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Contractor Cybersecurity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 41, United States Code, to require information technology contractors to maintain a vulnerability disclosure policy and program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T14:03:20Z"
    }
  ]
}
```
