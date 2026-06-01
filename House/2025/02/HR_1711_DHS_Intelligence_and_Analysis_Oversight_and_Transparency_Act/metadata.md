# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1711
- Title: DHS Intelligence and Analysis Oversight and Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 1711
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-05-15T16:50:22Z
- Update date including text: 2025-05-15T16:50:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-27 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-27 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1711",
    "number": "1711",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "DHS Intelligence and Analysis Oversight and Transparency Act",
    "type": "HR",
    "updateDate": "2025-05-15T16:50:22Z",
    "updateDateIncludingText": "2025-05-15T16:50:22Z"
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
          "name": "Counterterrorism and Intelligence Subcommittee",
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
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-27T18:44:37Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism and Intelligence Subcommittee",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1711ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1711\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Lee of Florida (for herself, Mr. Evans of Colorado , and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to direct the Under Secretary for Intelligence and Analysis of the Department of Homeland Security to conduct an annual audit of the information systems and bulk data of the Office of Intelligence and Analysis of the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DHS Intelligence and Analysis Oversight and Transparency Act .\n#### 2. Annual audit of DHS Office of Intelligence and Analysis information systems and bulk data\n##### (a) In general\nSubtitle A of title II of the Homeland Security Act of 2002 ( 6 U.S.C. 121 et seq. ) is amended by adding at the end the following:\n210H. Annual audit of information systems and bulk data (a) Definitions In this section: (1) Appropriate congressional committees The term appropriate congressional committees means the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate and the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives. (2) Bulk data The term bulk data means large quantities of data acquired without the use of discriminants, a significant portion of which are not reasonably likely to have intelligence or operational value. (3) Discriminants The term discriminants means identifiers and selection terms. (b) Annual audits Not later than 180 days after the date of the enactment of this section and annually thereafter, the Under Secretary for Intelligence and Analysis of the Department shall conduct an audit of the information systems and bulk data of the Office of Intelligence and Analysis, which shall be consistent with the intelligence oversight guidelines of the Office. (c) Notifications The Under Secretary for Intelligence and Analysis of the Department shall provide the appropriate congressional committees with\u2014 (1) a notification not later than 30 days after the first analysis or other intelligence use by the Office of Intelligence and Analysis after the date of the enactment of this section of any new bulk data set and the associated terms and conditions; and (2) an update not later than 30 days after any changes to such associated terms and conditions related to the use of such a bulk data set. (d) Reports and review (1) Reports to Congress Not later than 30 days after the conclusion of each audit under subsection (b), the Under Secretary for Intelligence and Analysis of the Department shall submit to the appropriate congressional committees the findings and results of such audit. (2) GAO review Not later than four years after the date of the enactment of this section, the Comptroller General of the United States shall provide the appropriate congressional committees a review of the implementation of the annual audit requirement under subsection (b), challenges to the implementation of such requirement, and recommendations for improving such audits. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 ( Public Law 107\u2013296 ; 116 Stat. 2135) is amended by inserting after the item relating to section 210G the following:\nSec.210H. Annual audit of information systems and bulk data. .",
      "versionDate": "2025-02-27",
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
        "updateDate": "2025-05-15T16:50:22Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1711ih.xml"
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
      "title": "DHS Intelligence and Analysis Oversight and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DHS Intelligence and Analysis Oversight and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to direct the Under Secretary for Intelligence and Analysis of the Department of Homeland Security to conduct an annual audit of the information systems and bulk data of the Office of Intelligence and Analysis of the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:19:12Z"
    }
  ]
}
```
