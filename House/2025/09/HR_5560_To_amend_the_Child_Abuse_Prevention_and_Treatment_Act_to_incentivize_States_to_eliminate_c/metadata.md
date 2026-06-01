# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5560?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5560
- Title: Statutes of Limitation for Child Sexual Abuse Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 5560
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-05-12T08:05:33Z
- Update date including text: 2026-05-12T08:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5560",
    "number": "5560",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Statutes of Limitation for Child Sexual Abuse Reform Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:33Z",
    "updateDateIncludingText": "2026-05-12T08:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:02:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "CO"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NE"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "DC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5560ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5560\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Subramanyam (for himself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Abuse Prevention and Treatment Act to incentivize States to eliminate civil and criminal statutes of limitations and revive time-barred civil claims for child abuse cases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Statutes of Limitation for Child Sexual Abuse Reform Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nChild sexual abuse is a pernicious crime perpetrated through threats of violence, intimidation, manipulation, and abuse of power.\n**(2)**\nChild sexual abuse is a public health epidemic that affects an estimated 1 in 4 girls and 1 in 20 boys in the United States.\n**(3)**\nThe prevalence of child sex trafficking is difficult to estimate, but the National Center for Missing and Exploited Children (NCMEC) reports receiving more than 19,000 reports of child sex trafficking in 2022.\n**(4)**\nHistorically, nearly 90 percent of child victims never go to the authorities and the vast majority of claims have expired before the victims were capable of getting to court.\n**(5)**\nDue to the subversive nature of this crime, the average age of disclosure of child sexual abuse does not occur until a victim is over 52 years old.\n**(6)**\nBecause many State statutes of limitations applicable to laws involving child sexual abuse fail to give victims adequate time to come forward and report their abuse, numerous victims are unable to seek fair and just remediation against their abusers.\n**(7)**\nDue to the especially heinous nature of child sexual abuse, it is imperative that perpetrators of this crime are punished, prevented from reoffending, and victims have the opportunity to see their abusers brought to justice.\n#### 3. Elimination of State statutes of limitations for child abuse cases\n##### (a) Child Abuse Prevention and Treatment Act\nSection 107(e)(1) of the Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5106c(e)(1) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) elimination of State civil and criminal statutes of limitations laws for child sexual abuse, exploitation, and sex trafficking, and adoption of laws reviving previously time-barred civil claims for child sexual abuse, exploitation, and sex trafficking. .\n##### (b) Special rule\nSection 111(b) of the Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5106g(b) ) is amended by adding at the end the following:\n(3) Child sexual abuse and exploitation For purposes of section 107(e)(1)(D), the term child sexual abuse and exploitation shall include an act or a failure to act on the part of a parent, caretaker, or any other person. .\n#### 4. Grants for eliminating certain statutes of limitation\n##### (a) Authorization\nThe Secretary of Health and Human Services may make grants to States that are eligible to receive an award under section 107 of the Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5106c ) to achieve one or more of the following reforms:\n**(1)**\nThe elimination of all State civil statutes of limitations for claims of, related to, or arising from, child sexual abuse, exploitation, and sex trafficking, against perpetrators, other individuals, and public and private entities.\n**(2)**\nThe elimination of all State criminal statutes of limitations for all felony and misdemeanor sex crimes against children, including sexual abuse, exploitation, and trafficking, and for inchoate offenses related to such sex crimes, including attempt, conspiracy, solicitation, and aiding and abetting.\n**(3)**\nThe revival of previously time-barred civil claims for child sexual abuse, exploitation, and sex trafficking against perpetrators, other individuals, and public and private entities, which, at a minimum, permits previously time-barred claims a 2-year period or until a victim reaches age 55, whichever is longer.\n##### (b) Allocation\nOf the funds made available to carry out this section\u2014\n**(1)**\n25 percent shall be for States that achieve one of the reforms described in paragraphs (1) through (3) of subsection (a);\n**(2)**\n35 percent shall be for States that achieve two of such reforms; and\n**(3)**\n40 percent shall be for States that achieve three of such reforms.\n42 U.S.C. 5106c\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $20,000,000 for each of fiscal years 2026 through 2033.\n#### 5. Technical correction\nSection 1404A of the Victims of Crime Act of 1984 ( 34 U.S.C. 20103 ), by striking section 109 and insert section 107 .",
      "versionDate": "2025-09-23",
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
        "name": "Families",
        "updateDate": "2026-04-01T13:32:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-23",
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
          "measure-id": "id119hr5560",
          "measure-number": "5560",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-23",
          "originChamber": "HOUSE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5560v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2025-09-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Statutes of Limitation for Child Sexual Abuse Reform Act</strong></p><p>This bill authorizes the Children's Bureau's Office of Child Abuse and Neglect to award grants to states to (1) eliminate their criminal and civil statutes of limitations for child sexual abuse, and (2) revive previously time-barred civil claims.</p><p>These grants are in addition to any funds a state is otherwise eligible to receive under the Children's Justice Act grant program, which provides grants to states to support the investigation and prosecution\u00a0of child abuse and neglect cases. The bill additionally requires states, as a condition of receiving funds under the Children's Justice Act grant program, to adopt recommendations from their program task force on\u00a0eliminating statutes of limitations for child sexual abuse claims and reviving previously time-barred civil claims.</p>"
        },
        "title": "Statutes of Limitation for Child Sexual Abuse Reform Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5560.xml",
    "summary": {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Statutes of Limitation for Child Sexual Abuse Reform Act</strong></p><p>This bill authorizes the Children's Bureau's Office of Child Abuse and Neglect to award grants to states to (1) eliminate their criminal and civil statutes of limitations for child sexual abuse, and (2) revive previously time-barred civil claims.</p><p>These grants are in addition to any funds a state is otherwise eligible to receive under the Children's Justice Act grant program, which provides grants to states to support the investigation and prosecution\u00a0of child abuse and neglect cases. The bill additionally requires states, as a condition of receiving funds under the Children's Justice Act grant program, to adopt recommendations from their program task force on\u00a0eliminating statutes of limitations for child sexual abuse claims and reviving previously time-barred civil claims.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hr5560"
    },
    "title": "Statutes of Limitation for Child Sexual Abuse Reform Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Statutes of Limitation for Child Sexual Abuse Reform Act</strong></p><p>This bill authorizes the Children's Bureau's Office of Child Abuse and Neglect to award grants to states to (1) eliminate their criminal and civil statutes of limitations for child sexual abuse, and (2) revive previously time-barred civil claims.</p><p>These grants are in addition to any funds a state is otherwise eligible to receive under the Children's Justice Act grant program, which provides grants to states to support the investigation and prosecution\u00a0of child abuse and neglect cases. The bill additionally requires states, as a condition of receiving funds under the Children's Justice Act grant program, to adopt recommendations from their program task force on\u00a0eliminating statutes of limitations for child sexual abuse claims and reviving previously time-barred civil claims.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hr5560"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5560ih.xml"
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
      "title": "Statutes of Limitation for Child Sexual Abuse Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Statutes of Limitation for Child Sexual Abuse Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Abuse Prevention and Treatment Act to incentivize States to eliminate civil and criminal statutes of limitations and revive time-barred civil claims for child abuse cases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:13Z"
    }
  ]
}
```
