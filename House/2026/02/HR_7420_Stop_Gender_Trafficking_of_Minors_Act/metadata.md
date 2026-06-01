# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7420
- Title: Stop Gender Trafficking of Minors Act
- Congress: 119
- Bill type: HR
- Bill number: 7420
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-03-19T15:14:49Z
- Update date including text: 2026-03-19T15:14:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7420",
    "number": "7420",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Gender Trafficking of Minors Act",
    "type": "HR",
    "updateDate": "2026-03-19T15:14:49Z",
    "updateDateIncludingText": "2026-03-19T15:14:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2026-02-09T17:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-09T17:01:00Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AZ"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7420ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7420\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Crenshaw (for himself, Mr. Crane , Mr. Fry , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend chapter 55 of title 18, United States Code, to establish a criminal offense for the transportation of a minor for a gender transition procedure.\n#### 1. Short title\nThis Act may be cited as the Stop Gender Trafficking of Minors Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nA growing body of international medical guidance has advised against the routine use of puberty blockers, hormone therapy, and gender altering surgeries for minors, absent long-term evidence of benefit and safety. The rise in detransition and regret among young adults who underwent such procedures as minors further underscores the need for robust Federal safeguards.\n**(2)**\nThe Federal Government has a compelling interest in protecting minors from experimental and irreversible medical procedures that may result in long-term harm, including sterilization, loss of sexual function, and psychological distress.\n**(3)**\nThe transportation of minors across state lines to receive such procedures constitutes interstate activity subject to Federal regulation under the Commerce Clause of the United States Constitution.\n#### 3. Transportation of a minor for gender a transition procedure\n##### (a) Offense\nChapter 55 of title 18, United States Code, is amended by adding at the end the following:\n1205 Transportation of a minor for a gender transition procedure (a) Offense Whoever knowingly transports in interstate or foreign commerce, or the offender travels in interstate or foreign commerce or uses the mail or any means, facility, or instrumentality of interstate or foreign commerce in committing or in furtherance of the commission of the offense, a minor to facilitate the minor in obtaining a gender transition procedure shall be fined under this title or imprisoned not more than ten years, or both. (b) Civil action A minor or a parent or legal guardian of a minor who has been transported in violation of subsection (a) may bring a civil action in an appropriate district court for injunctive relief, compensatory and punitive damages, and attorneys\u2019 fees. (c) Gender transition procedure defined In this section, the term gender transition procedure includes any medical or surgical intervention intended to alter the minor\u2019s sex characteristics in a manner inconsistent with the minor\u2019s biological sex, including: (1) Administration of puberty-blocking medications, including transportation relating to an appointment to obtain such medication or obtaining such medication. (2) Administration of cross-sex hormones. (3) A surgical intervention, including a mastectomy, phalloplasty, vaginoplasty, or other procedure intended to change primary or secondary sex characteristics. .\n##### (b) Federal funding prohibition\nNo Federal funds may be awarded to a State, unit of local government, or other governmental entity that:\n**(1)**\nEnacts, implements, or maintains a policy that permits or encourages a minor to undergo a gender transition procedure by being transported across State lines.\n**(2)**\nDeclares itself a sanctuary jurisdiction for a gender transition procedure.\n**(3)**\nDoes not cooperate with a Federal investigation of a violation of section 1205 of title 18, United States Code.\n**(4)**\nFails to cooperate with Federal investigations or enforcement actions related to this Act.\n##### (c) Gender transition procedure defined\nIn this section, the term gender transition procedure shall have the meaning given such term in section 1205 of title 18, United States Code.",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-19T15:14:48Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7420ih.xml"
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
      "title": "Stop Gender Trafficking of Minors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Gender Trafficking of Minors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 55 of title 18, United States Code, to establish a criminal offense for the transportation of a minor for a gender transition procedure.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:03:27Z"
    }
  ]
}
```
