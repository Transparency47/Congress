# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4190
- Title: Creating Early Childhood Leaders Act
- Congress: 119
- Bill type: S
- Bill number: 4190
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-05-29T15:12:45Z
- Update date including text: 2026-05-29T15:12:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4190",
    "number": "4190",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Creating Early Childhood Leaders Act",
    "type": "S",
    "updateDate": "2026-05-29T15:12:45Z",
    "updateDateIncludingText": "2026-05-29T15:12:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:22:54Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4190is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4190\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Kim (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to increase the knowledge and skills of principals and school leaders regarding early childhood education.\n#### 1. Short title\nThis Act may be cited as the Creating Early Childhood Leaders Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSince principals and school leaders have the second largest in-school impact on student achievement (after teachers), a principal or school leader's knowledge has a substantial impact on the teachers and students under the principal or school leader's supervision.\n**(2)**\nPrincipals and school leaders are increasingly being asked to supervise teachers and children in prekindergarten programs, yet school leaders often do not have training in early childhood education.\n**(3)**\nGiven the critical development that occurs in a child\u2019s early life and the impacts of this developmental period on later life outcomes, understanding the standards of early childhood education is particularly important.\n##### (b) Purpose\nThe purpose of this Act is to ensure that principals and school leaders are able to effectively support teachers in providing prekindergarten students with developmentally appropriate instruction.\n#### 3. School leader training regarding early childhood education\nSection 202(f)(1)(B) of the Higher Education Act of 1965 ( 20 U.S.C. 1022a(f)(1)(B) ) is amended\u2014\n**(1)**\nby striking clause (v) and inserting the following:\n(v) engage and involve parents, community members, the local educational agency, businesses, providers of early childhood education programs, and other community leaders, to leverage additional resources to improve student academic achievement; ;\n**(2)**\nin clause (vi), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(vii) understand child development, social and emotional development, developmentally appropriate behavioral interventions and supports, and effective instructional leadership skills for children from birth through age 8, in order to effectively manage and support developmentally appropriate early childhood education programs. .",
      "versionDate": "2026-03-25",
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
        "actionDate": "2026-05-15",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8859",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Creating Early Childhood Leaders Act",
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
        "name": "Education",
        "updateDate": "2026-04-09T14:54:24Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4190is.xml"
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
      "title": "Creating Early Childhood Leaders Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Early Childhood Leaders Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to increase the knowledge and skills of principals and school leaders regarding early childhood education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:37Z"
    }
  ]
}
```
