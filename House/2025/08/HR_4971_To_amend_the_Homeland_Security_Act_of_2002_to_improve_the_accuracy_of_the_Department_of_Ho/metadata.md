# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4971
- Title: Terrorist Watchlist Data Accuracy and Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 4971
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-05-16T08:08:02Z
- Update date including text: 2026-05-16T08:08:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-08-18 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-08-18 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4971",
    "number": "4971",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000193",
        "district": "2",
        "firstName": "Bennie",
        "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
        "lastName": "Thompson",
        "party": "D",
        "state": "MS"
      }
    ],
    "title": "Terrorist Watchlist Data Accuracy and Transparency Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:02Z",
    "updateDateIncludingText": "2026-05-16T08:08:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-18",
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
      "actionDate": "2025-08-15",
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
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-18T04:00:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4971ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4971\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Thompson of Mississippi introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to improve the accuracy of the Department of Homeland Security\u2019s terrorism screening information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terrorist Watchlist Data Accuracy and Transparency Act .\n#### 2. Quality assurance reviews of Department of Homeland Security nominations to the terrorist watchlist and other terrorism databases\n##### (a) In general\nSubtitle A of title II of the Homeland Security Act of 2002 ( 6 U.S.C. 121 et seq. ) is amended by adding at the end the following new section:\n210H. Quality assurance reviews of departmental nominations to the terrorist watchlist and other terrorism databases (a) Quality assurance reviews (1) In general Prior to submission to the Federal Bureau of Investigation\u2019s Terrorist Screening Center and the National Counterterrorism Center of an initial Department nomination of an individual for inclusion in the terrorist watchlist, including subsets of such watchlist, such as the No Fly List, the Selectee List, and watchlist exceptions, or other terrorism databases, or successors of such watchlist or other terrorism databases, the Secretary shall conduct a quality assurance review of such initial nomination to determine if all information contained in such initial Department nomination is free from error. (2) Submission of review and determination The Secretary shall ensure that reviews and determinations under paragraph (1) are included in each initial Department nomination submitted to the Federal Bureau of Investigation\u2019s Terrorist Screening Center and the National Counterterrorism Center. (b) Annual audits of United States persons nominations Not later than 90 days after the date of the enactment of this section and annually thereafter, the Secretary, acting through the Under Secretary for Intelligence and Analysis, shall review, as of the date of each such review, all Department nominations of United States persons for inclusion in the terrorist watchlist, including subsets of such watchlist, such as the No Fly List, the Selectee List, and watchlist exceptions, or other terrorism databases, or successors of such watchlist or other terrorism databases, and determine the following for each such nomination: (1) If all information contained in each such Department nomination is free from error. (2) If each such Department nomination continues to satisfy the criteria specified in the Watchlisting Advisory Council\u2019s Watchlisting Guidance for such inclusion. (c) Random audits Not later than 90 days after the date of the enactment of this section and monthly thereafter, the Secretary, acting through the Under Secretary for Intelligence and Analysis, shall establish a random audit program to periodically review, as of the date of each such review, all Department nominations of individuals for inclusion in the terrorist watchlist, including subsets of such watchlist, such as the No Fly List, the Selectee List, and watchlist exceptions, or other terrorism databases, or successors of such watchlist or other terrorism databases, and determine the following for each such Department nomination: (1) If all information contained in each such Department nomination is free from error. (2) If each such Department nomination continues to satisfy the criteria referred to in subsection (b)(2) for such inclusions. (d) Correcting or retracting records The Secretary, acting through the Under Secretary for Intelligence and Analysis, shall notify the Federal Bureau of Investigation\u2019s Terrorist Screening Center and the National Counterterrorism Center not later than 24 hours after making a determination in the negative pursuant to subsection (b) or (c), as the case may be, with respect to a Department nomination of an individual for inclusion in the terrorist watchlist, including subsets of such watchlist, such as the No Fly List, the Selectee List, and watchlist exceptions, or other terrorism databases, or successors of such watchlist or other terrorism databases, and include in any such notification a request, if appropriate, for an associated correction or retraction with respect to such inclusion. (e) Consultation with FBI and NCTC If the Secretary determines a correction or retraction, as appropriate and as the case may be, under subsection (d) with respect to the inclusion of an individual in the terrorist watchlist, including subsets of such watchlist, such as the No Fly List, the Selectee List, and watchlist exceptions, or other terrorism databases, or successors of such watchlist or other terrorism databases has not been effectuated by the date that is 30 days after a request relating thereto was made pursuant to such subsection, the Secretary shall promptly consult with the Director of the Federal Bureau of Investigation or the Director of the National Counterterrorism Center, as appropriate, regarding any decision or justification by either such Director, as appropriate, relating to such correction or retraction, as the case may be. (f) Report to Congress The Secretary shall annually submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report containing information relating to the number of identities, disaggregated by United States person identities and non-United States person identities, referred for corrections or retractions pursuant to this section, and the number of nominations recalled or reissued as a result of such referrals. (g) Definitions In this section: (1) Terrorist watchlist The term terrorist watchlist has the meaning given the term terrorist screening database in section 2101. (2) Other terrorism databases The term other terrorism databases means the Terrorist Identities Datamart Environment or any other database maintained by the National Counterterrorism Center pursuant to section 119(d)(6) of the National Security Act of 1947 ( 50 U.S.C. 3056(d)(6) ). (3) United States person The term United States person means any United States citizen or alien admitted for permanent residence in the United States. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 210G the following new item:\nSec. 210G. Quality assurance reviews of departmental nominations to the terrorist watchlist and other terrorism databases. .",
      "versionDate": "2025-08-15",
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
        "updateDate": "2026-03-27T19:10:19Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4971ih.xml"
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
      "title": "Terrorist Watchlist Data Accuracy and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Terrorist Watchlist Data Accuracy and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to improve the accuracy of the Department of Homeland Security's terrorism screening information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T04:33:20Z"
    }
  ]
}
```
