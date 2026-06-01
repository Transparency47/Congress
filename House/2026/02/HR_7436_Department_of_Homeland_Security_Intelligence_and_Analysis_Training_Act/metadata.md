# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7436?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7436
- Title: Department of Homeland Security Intelligence and Analysis Training Act
- Congress: 119
- Bill type: HR
- Bill number: 7436
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-21T08:08:07Z
- Update date including text: 2026-05-21T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7436",
    "number": "7436",
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
    "title": "Department of Homeland Security Intelligence and Analysis Training Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:07Z",
    "updateDateIncludingText": "2026-05-21T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
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
          "date": "2026-02-09T17:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-14T14:01:45Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T14:01:27Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-10T15:01:08Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
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
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7436ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7436\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Magaziner (for himself, Mr. Pfluger , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to direct the Secretary of Homeland Security to implement a standardized training program for employees of the Office of Intelligence and Analysis of the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Department of Homeland Security Intelligence and Analysis Training Act .\n#### 2. Formalized and standardized training curricula\n##### (a) In general\nSection 201 of the Homeland Security Act of 2002 ( 6 U.S.C. 121 ) is amended by\u2014\n**(1)**\nredesignating subsections (f) and (g) as subsections (g) and (h), respectively; and\n**(2)**\ninserting after subsection (e) the following new subsection:\n(f) Office of Intelligence and Analysis employee training (1) Standardized training The Secretary, acting through the Under Secretary for Intelligence and Analysis, shall implement a standardized entry-level basic intelligence training curricula for all employees of the Office of Intelligence and Analysis. Such training shall\u2014 (A) be provided to all new hires within the Office of Intelligence and Analysis and, for each such new hire, shall commence not later than 90 days after the official start date of each such new hire and before the beginning of official duties of each such new hire; and (B) include training on civil rights, civil liberties, privacy rights, regulations, and information practices pursuant to section 552a of title 5, United States Code (commonly referred to as the Privacy Act of 1974 ), and other relevant laws. (2) Analyst training In addition to the standardized entry-level basic intelligence training required under paragraph (1), all new hires appointed to an analytic position within the Office of Intelligence and Analysis shall receive training that includes education and training on the following: (A) The role of the Department and the Office of Intelligence and Analysis\u2019s mission to integrate intelligence into operations across the Department and disseminate such intelligence to State, local, Tribal, and territorial partners and private sector partners to identify, mitigate, and respond to threats to the homeland. (B) Intelligence community analytic standards, including methodologies, outreach, sourcing requirements for disseminated analytical products, writing standards, and competency directories for the intelligence community. (3) Open source intelligence collection training In addition to the standardized entry-level basic intelligence training required under paragraph (1), all new hires appointed to an open source intelligence collection position within the Office of Intelligence and Analysis shall receive training that includes education and training on the following: (A) The basic principles and techniques of open source intelligence collection, including how, in accordance with constitutional and legal parameters and relevant Federal and departmental policies regarding privacy, civil rights, and civil liberties protections, to effectively navigate unclassified, publicly available information sources. (B) Data management principles, including the proper protocols regarding how, in accordance with relevant Federal law and policy regarding privacy, civil rights, and civil liberties protections, to use data, information, and knowledge appropriately, including storage and retention. (C) Intelligence community open source intelligence collection standards and the Department\u2019s statutory authority regarding open source intelligence collection in accordance with subsection (d)(19)(A). (4) Specialized and advanced training The Secretary, acting through the Under Secretary for Intelligence and Analysis, shall\u2014 (A) develop and make available specialized and advanced training curricula, including raw intelligence release authority training, to improve the activities and operations of the Office of Intelligence and Analysis and promote professional development among employees of the Office of Intelligence and Analysis; and (B) on a quarterly basis, make publicly available to employees of the workforce of the Office of Intelligence and Analysis a list of available specialized training provided by\u2014 (i) other elements of the intelligence community; and (ii) the Department of Defense. (5) Provision of training to non-Office of Intelligence and Analysis employees within the Department The Secretary, acting through the Under Secretary for Intelligence and Analysis, may, pursuant to section 208, provide to employees, officials, and other senior executives of the intelligence components of the Department training developed pursuant to this subsection. (6) Tracking training progress The Secretary, acting through the Under Secretary for Intelligence and Analysis, shall implement a system to track the progress of completion by employees of the Office of Intelligence and Analysis of training provided by\u2014 (A) the Department; (B) other elements of the intelligence community; and (C) the Department of Defense. (7) Implementation This subsection shall take effect on the date that is one year after the date of the enactment of this subsection and apply to employees of the Office of Intelligence and Analysis, as follows: (A) Any individual appointed to a position in the Office on or after the date of enactment of this subsection, any employee of the Office on such date who has been employed by the Office for two years or less, and any employee of the Office occupying a position classified below grade GS\u201312 of the General Schedule (or equivalent) shall complete standardized entry-level basic intelligence training under paragraph (1). (B) All employees of the Office, as appropriate, shall complete analyst training and open source intelligence collection training pursuant to paragraphs (2) and (3), respectively. (8) Reports Not later than two years after the date of the enactment of this subsection and annually thereafter for five years, the Under Secretary for Intelligence and Analysis shall submit to the appropriate congressional committees a report on the implementation of this subsection. Each such report shall include the following: (A) A description of the curricula developed for standardized entry-level basic intelligence training, as well as analyst training, open source intelligence collection training, and specialized or advanced training courses pursuant to paragraph (1), (2), (3), and (4), respectively, provided by the Office of Intelligence and Analysis. (B) Information relating to the number of individuals who completed\u2014 (i) specialized or advanced training courses, including release authority training, pursuant to paragraph (4); and (ii) other training offered by\u2014 (I) other elements of the intelligence community; and (II) the Department of Defense. (C) Information on the extent to which employees of other intelligence components of the Department receive training developed pursuant to this subsection. (9) Definitions In this subsection: (A) Appropriate congressional committees The term appropriate congressional committees means\u2014 (i) the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives; and (ii) the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate. (B) Intelligence community The term intelligence community has the meaning given such term in section 3(4) of the National Security Act of 1947 ( 50 U.S.C. 3003(4) ). .\n##### (b) Comptroller general review\nNot later than two years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate a report on the implementation of subsection (f) of section 201 of the Homeland Security Act of 2002 ( 6 U.S.C. 121 ), as added by this Act. Such report shall compare the curriculum of training provided pursuant to such subsection (f) with training provided by other elements of the intelligence community (as such term is defined in section 3(4) of the National Security Act of 1947) and the Department of Defense, as well as with training provided by the Office of Intelligence and Analysis of the Department of Homeland Security as of such date of enactment. Such report shall also consider the approach taken by the Office of Intelligence and Analysis to ensure training provided pursuant to such subsection (f) is completed in accordance with such subsection, and identify ways to improve the management of such training based on best practices by such other elements of the intelligence community and the Department of Defense.",
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
        "updateDate": "2026-02-18T16:05:32Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7436ih.xml"
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
      "title": "Department of Homeland Security Intelligence and Analysis Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T04:43:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Department of Homeland Security Intelligence and Analysis Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T04:43:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to direct the Secretary of Homeland Security to implement a standardized training program for employees of the Office of Intelligence and Analysis of the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:18:38Z"
    }
  ]
}
```
