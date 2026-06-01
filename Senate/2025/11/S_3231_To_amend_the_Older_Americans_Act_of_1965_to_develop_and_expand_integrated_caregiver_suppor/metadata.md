# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3231
- Title: Respite CARE Act
- Congress: 119
- Bill type: S
- Bill number: 3231
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-02T14:57:13Z
- Update date including text: 2025-12-02T14:57:13Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3231",
    "number": "3231",
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
    "title": "Respite CARE Act",
    "type": "S",
    "updateDate": "2025-12-02T14:57:13Z",
    "updateDateIncludingText": "2025-12-02T14:57:13Z"
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
          "date": "2025-11-20T17:01:08Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3231is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3231\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Markey (for himself, Mrs. Gillibrand , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to develop and expand integrated caregiver support services for family caregivers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Respite Care and Resources for Everyone Act or the Respite CARE Act .\n#### 2. Caregiver support\nTitle IV of the Older Americans Act of 1965 is amended by inserting after section 414 ( 42 U.S.C. 3032c ) the following:\n415. Caregiver support (a) Grants The Assistant Secretary may make grants to eligible entities for the development or expansion of integrated caregiver support services, through which a provider provides, at the same time and integrated setting, respite care to assist family caregivers and other supportive services or support services described in section 373(b) for family caregivers. (b) Eligible entity To be eligible to receive a grant under subsection (a), an entity shall be a State or local government agency, a nonprofit organization, an area agency on aging, the provider of a multipurpose senior center, an institution of higher education, or a Tribal organization. (c) Application To be eligible to receive a grant under subsection (a), an entity shall submit an application to the Assistant Secretary at such time, in such manner, and containing such information as the Assistant Secretary may require. (d) Use of funds An eligible entity receiving a grant under subsection (a) shall use the grant funds, consistent with subsection (e)\u2014 (1) to develop or expand integrated caregiver support services in order to provide respite care at the same time and integrated setting as supportive services or support services described in section 373(b) for family caregivers; and (2) to provide services described in paragraph (1) in a manner that is accessible, as appropriate for the family caregiver or the care recipient, as the case may be, including providing the services\u2014 (A) through assistive technology; (B) in an accessible language; (C) for caregivers for whom English is not their primary language, through translation or interpretation services; and (D) in an accessible format, including formats compatible with American Sign Language and multiple languages. (e) Direct or indirect provision An eligible entity receiving such a grant may use the grant funds directly, or indirectly by contract with a health care provider or child care provider, to provide respite care. (f) Definitions In this section: (1) Caregiver support services The term caregiver support services means services, provided for a family caregiver, that are\u2014 (A) supportive services; or (B) support services described in section 373(b). (2) Child care provider (A) In general The term child care provider means a center-based child care provider, a family child care provider, or other provider of child care services for compensation that\u2014 (i) is licensed to provide child care services under State law applicable to the child care services it provides or, in the case of an Indian Tribe or Tribal organization, meets the rules set by the Secretary of Health and Human Services; (ii) participates in the State\u2019s tiered system for recognizing and supporting the quality of child care services, or, in the case of an Indian Tribe or Tribal organization, meets the rules set by the Secretary, on such schedule as the Secretary may provide; and (iii) satisfies the State and local requirements, including those requirements described in section 658E(c)(2)(I) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c(c)(2)(I) ), applicable to the child care services it provides. (B) Family child care provider In subparagraph (A), the term family child care provider means one or more individuals who provide child care services, in a private residence other than the residences of the children involved, for less than 24 hours per day per child, or for 24 hours per day per child due to the nature of the work of the parent involved. (3) Family caregiver The term family caregiver \u2014 (A) means\u2014 (i) an adult family member, or another individual, who is an informal provider of in-home and community care to an older individual or to an individual of any age with Alzheimer's disease or a related disorder with neurological and organic brain dysfunction; or (ii) an older relative caregiver; and (B) does not include an individual providing care whose primary relationship with the individual receiving the care is based on a financial or professional agreement. (4) Health care provider The term health care provider means a health care provider, as defined in section 3000 of the Public Health Service Act ( 42 U.S.C. 300jj ) or a Federally qualified health center, as defined in section 1861 of the Social Security Act ( 42 U.S.C. 1395x ). (5) Indian tribe, tribal organization The terms Indian Tribe and Tribal organization have the meanings given the terms Indian tribe and tribal organization , respectively, in section 658P of such Act ( 42 U.S.C. 9858n ). (6) Older relative caregiver The term older relative caregiver \u2014 (A) means a caregiver who\u2014 (i) is age 55 or older; and (ii) lives with, is the informal provider of in-home and community care to, and is the primary caregiver for, a child or an individual with a disability; (B) in the case of a caregiver for a child\u2014 (i) is the grandparent, stepgrandparent, or other relative (other than the parent) by blood, marriage, or adoption, of the child; (ii) is the primary caregiver of the child because the biological or adoptive parents are unable or unwilling to serve as the primary caregivers of the child; and (iii) has a legal relationship to the child, such as legal custody, adoption, or guardianship, or is raising the child informally; and (C) in the case of a caregiver for an individual with a disability, is the parent, grandparent, or other relative by blood, marriage, or adoption, of the individual with a disability. (7) Respite care The term respite care means care, which may include health care and child care, for a care recipient of a family caregiver. .",
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
        "updateDate": "2025-12-02T14:57:13Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3231is.xml"
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
      "title": "Respite CARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respite CARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respite Care and Resources for Everyone Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act of 1965 to develop and expand integrated caregiver support services for family caregivers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:20Z"
    }
  ]
}
```
