# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3233
- Title: FINANCE Act
- Congress: 119
- Bill type: S
- Bill number: 3233
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-06T13:40:28Z
- Update date including text: 2025-12-06T13:40:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3233",
    "number": "3233",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "FINANCE Act",
    "type": "S",
    "updateDate": "2025-12-06T13:40:28Z",
    "updateDateIncludingText": "2025-12-06T13:40:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T17:03:26Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3233is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3233\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Markey (for himself, Ms. Klobuchar , Mrs. Gillibrand , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to provide financial planning services related to the needs of family caregivers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Services Improving Noble and Necessary Caregiving Experience Act or the FINANCE Act .\n#### 2. Financial planning services\nTitle IV of the Older Americans Act of 1965 is amended by inserting after section 414 ( 42 U.S.C. 3032c ) the following:\n415. Financial planning services (a) Definitions In this section: (1) The term family caregiver \u2014 (A) means\u2014 (i) an adult family member, or another individual, who is an informal provider of in-home and community care to an older individual or to an individual of any age with Alzheimer's disease or a related disorder with neurological and organic brain dysfunction; or (ii) an older relative caregiver; and (B) does not include an individual providing care whose primary relationship with the individual receiving the care is based on a financial or professional agreement. (2) The term older relative caregiver means a caregiver who\u2014 (A) (i) is age 55 or older; and (ii) lives with, is the informal provider of in-home and community care to, and is the primary caregiver for, a child or an individual with a disability; (B) in the case of a caregiver for a child\u2014 (i) is the grandparent, stepgrandparent, or other relative (other than the parent) by blood, marriage, or adoption, of the child; (ii) is the primary caregiver of the child because the biological or adoptive parents are unable or unwilling to serve as the primary caregivers of the child; and (iii) has a legal relationship to the child, such as legal custody, adoption, or guardianship, or is raising the child informally; and (C) in the case of a caregiver for an individual with a disability, is the parent, grandparent, or other relative by blood, marriage, or adoption, of the individual with a disability. (b) Grants The Assistant Secretary may make grants to eligible entities to provide financial planning services related to the needs of family caregivers. (c) Eligible entity To be eligible to receive a grant under subsection (b), an entity shall be a State or local government agency, a nonprofit organization, an area agency on aging, the provider of a multipurpose senior center, an institution of higher education, or a tribal organization. (d) Application To be eligible to receive a grant under subsection (b), an entity shall submit an application to the Assistant Secretary at such time, in such manner, and containing such information as the Assistant Secretary may require. (e) Use of funds An eligible entity that receives a grant under subsection (b) shall use the grant funds\u2014 (1) to provide financial planning services, through individuals with the appropriate training and licenses, that include\u2014 (A) guidance on available public benefits; (B) guidance on care options, including on supports for paid and unpaid family caregivers; (C) information on budgeting, saving, and spending; (D) information on how and when to begin talking about desires and wishes around care as an individual ages; (E) guidance on managing debt, debt relief, and bankruptcy; (F) information and education on what long-term care will cost; (G) resources and information, including outreach materials, technical assistance materials, and other resources and information available through the center referred to in section 215(k); and (H) referrals to providers of legal assistance under title III or VII, for legal assistance on topics including estate planning, power of attorney, health care powers, and wills; and (2) to provide those services in a manner that is accessible, as appropriate for the recipient, including providing the services\u2014 (A) through assistive technology; (B) in accessible language; (C) for caregivers for whom English is not their primary language, through translation or interpretation services; and (D) for caregivers, in accessible formats, including formats compatible with American Sign Language and multiple languages. .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "name": "Social Welfare",
        "updateDate": "2025-12-06T13:40:28Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3233is.xml"
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
      "title": "FINANCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FINANCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Services Improving Noble and Necessary Caregiving Experience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act of 1965 to provide financial planning services related to the needs of family caregivers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T04:03:51Z"
    }
  ]
}
```
