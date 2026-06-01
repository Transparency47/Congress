# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6194?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6194
- Title: Protecting Americans from Russian Litigation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6194
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-01T16:20:54Z
- Update date including text: 2026-05-01T16:20:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6194",
    "number": "6194",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "H001095",
        "district": "38",
        "firstName": "Wesley",
        "fullName": "Rep. Hunt, Wesley [R-TX-38]",
        "lastName": "Hunt",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protecting Americans from Russian Litigation Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-01T16:20:54Z",
    "updateDateIncludingText": "2026-05-01T16:20:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
        "item": [
          {
            "date": "2026-03-26T18:34:19Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-20T15:11:25Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6194ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6194\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Hunt (for himself, Mr. Fitzgerald , Mr. Gill of Texas , Ms. Lee of Florida , Mr. Nadler , Mr. Lieu , and Ms. Kamlager-Dove ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit the availability of civil actions affected by United States sanctions.\n#### 1. Short title\nThis Act may be cited as the Protecting Americans from Russian Litigation Act of 2025 .\n#### 2. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto ensure that United States persons are not disadvantaged for actions or omissions undertaken to comply with United States sanctions or export controls; and\n**(2)**\nto ensure that foreign persons, or persons acting on their behalf, cannot obtain compensation for any action related to United States persons attempting in good faith to comply with their obligations under United States sanctions or export controls.\n#### 3. Limitation on civil actions affected by United States sanctions\n##### (a) In general\nChapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Limitation on civil actions affected by United States sanctions (a) Limitation Notwithstanding any provision of law, no person (other than the United States or a person acting on behalf of the United States) may bring a civil action in Federal or State court to enforce any foreign judgment or foreign arbitral award arising from a claim where\u2014 (1) the underlying conduct or circumstances giving rise to the claim resulted from actions to comply with United States sanctions impeding the performance of a contract; or (2) the court or tribunal issuing the judgment or arbitral award asserted jurisdiction based, in whole or in part, on the imposition of United States sanctions or export controls (or any foreign law enacted in response to the imposition of United States sanctions or export controls). (b) Removal and dismissal An action to recognize or enforce a foreign judgment or foreign arbitral award described in subsection (a) may be removed by any defendant to the appropriate United States district court, which shall dismiss the action. (c) Rule of construction Nothing in this section may be construed to limit\u2014 (1) the authority of the President, any delegate of the President (including the Office of Foreign Assets Control of the Department of the Treasury), or any other officer or official of the United States to bring any action or exercise any responsibility under any applicable State or Federal law; (2) any right, remedy, or cause of action available to a victim of international terrorism, torture, extrajudicial killing, aircraft sabotage, or hostage taking, who is, or was at the time of the victim\u2019s injury, a national of the United States, a member of the United States Armed Forces, an employee of the United States Government, or an individual performing a contract awarded by the United States Government acting within the scope of the individual's employment, or a family member of any such victim, under any applicable State or Federal law, including\u2014 (A) chapter 97 of this title; (B) chapter 113B of title 18; and (C) the Iran Threat Reduction and Syria Human Rights Act of 2012 ( 22 U.S.C. 8701 et seq. ) and any other laws providing for the application of sanctions with respect to Iran or Syria; (3) any right, remedy, or cause of action available to any party arising under or relating to the party\u2019s contractual rights (other than an action to enforce a foreign judgment or foreign arbitral award described in subsection (a)) where the parties agreed to resolve all disputes by litigation in a State or Federal court within the United States or by arbitration within the United States; or (4) any other right, remedy, or cause of action available to any party arising under State or Federal law (other than an action to enforce a foreign judgment or foreign arbitral award described in subsection (a)) where the underlying conduct or circumstances giving rise to the claim resulted from the imposition of United States sanctions or export controls. (d) United states sanctions defined In this section: (1) In general The term United States sanctions means any prohibition, restriction, or condition on transactions involving any property in which any foreign country or national thereof has any interest that is imposed by the United States to address threats to the national security, foreign policy, or economy of the United States pursuant to\u2014 (A) section 203 of the International Emergency Economic Powers Act ( 50 U.S.C. 1702 ); or (B) any other provision of law, including any provision of law relating to export controls. (2) Duties The term United States sanctions does not include the imposition of a duty on the importation of goods. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by inserting after the item relating to section 1659 the following new item:\n1660. Limitation on civil actions affected by United States sanctions. .\n##### (c) Application\nSection 1660 of title 28, United States Code, as added by subsection (a), applies with respect to civil actions pending on or after the date of the enactment of this Act.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2026-04-28",
        "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2073-2074; text: CR S2073-2074)"
      },
      "number": "2934",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Americans from Russian Litigation Act of 2025",
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
            "updateDate": "2026-05-01T14:25:36Z"
          },
          {
            "name": "Contracts and agency",
            "updateDate": "2026-05-01T14:25:44Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-05-01T14:25:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2026-05-01T13:13:23Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6194ih.xml"
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
      "title": "Protecting Americans from Russian Litigation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T08:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Americans from Russian Litigation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T08:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the availability of civil actions affected by United States sanctions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T08:33:34Z"
    }
  ]
}
```
