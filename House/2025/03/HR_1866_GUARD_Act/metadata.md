# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1866
- Title: GUARD Act
- Congress: 119
- Bill type: HR
- Bill number: 1866
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-05T22:05:05Z
- Update date including text: 2025-12-05T22:05:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1866",
    "number": "1866",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "GUARD Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:05:05Z",
    "updateDateIncludingText": "2025-12-05T22:05:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:06:25Z",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "OK"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1866ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1866\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Hageman (for herself, Mrs. Miller of Illinois , Mr. Grothman , Mrs. Biggs of South Carolina , Mr. Brecheen , Mr. Gill of Texas , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Abuse Prevention and Treatment Act to disqualify any State that discriminates against parents or guardians who oppose medical, surgical, pharmacological, psychological treatment, or clothing and social changes related to affirming the subjective claims of gender identity expressed by any minor if such claimed identity is inconsistent with such minor\u2019s biological sex from receiving funding under such Act.\n#### 1. Short title\nThis Act may be cited as the Guaranteeing Unalienable and Anatomical Rights for Dependents Act or the GUARD Act .\n#### 2. State grant requirements\nThe Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5101 et seq. ) is amended by inserting after section 3 the following:\n4. State grant requirements (a) In general Notwithstanding any other provision of law, no State may receive funding under this Act if such State takes any adverse action or otherwise discriminates against parents, guardians, or legal representatives who oppose medical, surgical, pharmacological, psychological treatment, or other medical intervention, or clothing, name or pronoun use, or other social changes or practices related to transitioning to or affirming the claims or expressions of gender identity of any minor under the charge, care, or supervision of the parent, guardian, or legal representative, if such gender identity is inconsistent, in such parent's, guardian's, or legal representative's estimation, with such minor\u2019s biological sex, as determined definitively at or before birth, regardless of any medical diagnosis or indication of gender dysphoria, body dysphoria, dissociative identity disorder, or social anxiety disorder. (b) Enforcement In the case of an award made by the Secretary under this Act in violation of subsection (a), any parent, guardian, or legal representative who experienced an adverse action or other discrimination described in subsection (a) by a State receiving funding under this Act may bring an action, in an appropriate Federal district court of the United States or State court, against the Department of Health and Human Services, seeking to enjoin the Secretary from continuing such award to such State and to require the State awarded amounts in violation of subsection (a) to return such funds to the Treasury. .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "851",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GUARD Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-03-21T17:40:46Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1866ih.xml"
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
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guaranteeing Unalienable and Anatomical Rights for Dependents Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Abuse Prevention and Treatment Act to disqualify any State that discriminates against parents or guardians who oppose medical, surgical, pharmacological, psychological treatment, or clothing and social changes related to affirming the subjective claims of gender identity expressed by any minor if such claimed identity is inconsistent with such minor's biological sex from receiving funding under such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:30Z"
    }
  ]
}
```
