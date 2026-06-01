# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/851?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/851
- Title: GUARD Act
- Congress: 119
- Bill type: S
- Bill number: 851
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-12-05T22:08:56Z
- Update date including text: 2025-12-05T22:08:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/851",
    "number": "851",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "GUARD Act",
    "type": "S",
    "updateDate": "2025-12-05T22:08:56Z",
    "updateDateIncludingText": "2025-12-05T22:08:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-05T16:34:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "AR"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s851is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 851\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Banks (for himself, Mr. Cotton , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Child Abuse Prevention and Treatment Act to disqualify any State that discriminates against parents or guardians who oppose medical, surgical, pharmacological, psychological treatment, or clothing and social changes related to affirming the subjective claims of gender identity expressed by any minor if such claimed identity is inconsistent with such minor\u2019s biological sex from receiving funding under such Act.\n#### 1. Short title\nThis Act may be cited as the Guaranteeing Unalienable and Anatomical Rights for Dependents Act or the GUARD Act .\n#### 2. State grant requirements\nThe Child Abuse Prevention and Treatment Act ( 42 U.S.C. 5101 et seq. ) is amended by inserting after section 3 the following:\n4. State grant requirements (a) In general Notwithstanding any other provision of law, no State may receive funding under this Act if such State takes any adverse action or otherwise discriminates against parents, guardians, or legal representatives who oppose medical, surgical, pharmacological, psychological treatment, or other medical intervention, or clothing, name or pronoun use, or other social changes or practices related to transitioning to or affirming the claims or expressions of gender identity of any minor under the charge, care, or supervision of the parent, guardian, or legal representative, if such gender identity is inconsistent, in such parent's, guardian's, or legal representative's estimation, with such minor\u2019s biological sex, as determined definitively at or before birth, regardless of any medical diagnosis or indication of gender dysphoria, body dysphoria, dissociative identity disorder, or social anxiety disorder. (b) Enforcement In the case of an award made by the Secretary under this Act in violation of subsection (a), any parent, guardian, or legal representative who experienced an adverse action or other discrimination described in subsection (a) by a State receiving funding under this Act may bring an action, in an appropriate Federal district court of the United States or State court, against the Department of Health and Human Services, seeking to enjoin the Secretary from continuing such award to such State and to require the State awarded amounts in violation of subsection (a) to return such funds to the Treasury. .",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1866",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GUARD Act",
      "type": "HR"
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
        "updateDate": "2025-03-28T11:47:49Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s851is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-03-27T03:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guaranteeing Unalienable and Anatomical Rights for Dependents Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Child Abuse Prevention and Treatment Act to disqualify any State that discriminates against parents or guardians who oppose medical, surgical, pharmacological, psychological treatment, or clothing and social changes related to affirming the subjective claims of gender identity expressed by any minor if such claimed identity is inconsistent with such minor's biological sex from receiving funding under such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:03:31Z"
    }
  ]
}
```
