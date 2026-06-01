# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/503
- Title: Qualified Immunity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 503
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-10-25T08:05:24Z
- Update date including text: 2025-10-25T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/503",
    "number": "503",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Qualified Immunity Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:24Z",
    "updateDateIncludingText": "2025-10-25T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IN"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "AZ"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MS"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr503ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 503\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Foxx (for herself and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Revised Statutes to codify the defense of qualified immunity in the case of any action under section 1979, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Qualified Immunity Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nQualified immunity is intended for all but the plainly incompetent or those who knowingly violate the law and is meant to give government officials breathing room to make reasonable mistakes of fact and law.\n**(2)**\nThe Supreme Court has observed that qualified immunity balances two important interests, the need to hold law enforcement officers accountable when they exercise power irresponsibly and the need to shield officers from harassment, distraction, and liability when they perform their duties reasonably.\n#### 3. Codification of qualified immunity\n##### (a) In general\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nby inserting (a) In general\u2014 before Every person ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) Applicability to law enforcement officers (1) A law enforcement officer subject to an action under this section in their individual capacity shall not be found liable if such law enforcement officer establishes that\u2014 (A) the right, privilege, or immunity secured by the Constitution or Federal law was not clearly established at the time of their deprivation by the law enforcement officer, or that at this time, the state of the law was not sufficiently clear that every reasonable law enforcement officer would have understood that the conduct alleged constituted a violation of the Constitution or Federal law; or (B) a court of competent jurisdiction had issued a final decision on the merits holding, without reversal, vacatur, or preemption, that the specific conduct alleged to be unlawful was consistent with the Constitution and Federal laws. (2) A law enforcement agency or unit of local government who employed a law enforcement officer subject to an action under subsection (a), shall not be liable for such action if the law enforcement officer is found not liable under paragraph (1) and was acting within the scope of their employment. (c) Definitions In this section: (1) Law enforcement officer The term law enforcement officer means any Federal, State, Tribal, or local official who is authorized by law to engage in or supervise the prevention, detection, investigation, or the incarceration of any person for any violation of law, and has the statutory powers of arrest or apprehension, including police officers and other agents of a law enforcement agency. (2) Law enforcement agency The term law enforcement agency means any Federal, State, Tribal, or local public agency engaged in supervision, prevention, detection, investigation, or the incarceration of any person for any violation of law, and has the statutory powers of arrest or apprehension. .\n##### (b) Effective date\nThe amendments made under subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "122",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Qualified Immunity Act of 2025",
      "type": "S"
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
            "name": "Civil actions and liability",
            "updateDate": "2025-02-13T19:55:59Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-02-13T19:55:59Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-02-13T19:55:59Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-02-13T19:55:59Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-02-13T19:55:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-02-13T19:47:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr503",
          "measure-number": "503",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr503v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that\u00a0every reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>"
        },
        "title": "Qualified Immunity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr503.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that\u00a0every reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr503"
    },
    "title": "Qualified Immunity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that\u00a0every reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr503"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr503ih.xml"
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
      "title": "Qualified Immunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Qualified Immunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Revised Statutes to codify the defense of qualified immunity in the case of any action under section 1979, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T05:18:23Z"
    }
  ]
}
```
