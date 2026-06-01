# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5809
- Title: Fight Hunger Act
- Congress: 119
- Bill type: HR
- Bill number: 5809
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2025-11-20T17:59:33Z
- Update date including text: 2025-11-20T17:59:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5809",
    "number": "5809",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Fight Hunger Act",
    "type": "HR",
    "updateDate": "2025-11-20T17:59:33Z",
    "updateDateIncludingText": "2025-11-20T17:59:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5809ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5809\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Thanedar introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against tax for food donations.\n#### 1. Short title\nThis Act may be cited as the Fight Hunger Act .\n#### 2. Tax credit for donations to charitable organizations that feed ill, needy, or infants\n##### (a) In general\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n30E. Donations to charitable organizations that feed ill, needy, or infants (a) In general In the case of a taxpayer who elects the application of this section, there shall be allowed as a credit against the tax imposed by this chapter an amount equal to the qualified charitable donations made by the taxpayer during the taxable year. (b) Qualified charitable donations (1) In general For purposes of this section, the term qualified charitable donation means any charitable contribution (as defined in section 170(c)) to an organization which is described in section 501(c)(3) and exempt from tax under section 501(a) (other than a private foundation, as defined in section 509(a), which is not an operating foundation, as defined in section 4942(j)(3)), but only if\u2014 (A) such contribution is\u2014 (i) made in cash, or (ii) is food that is apparently wholesome food, and (B) (i) such contribution is to an organization that is a food bank, soup kitchen, or other organizations that would typically receive donations of food to carry out the purpose or function constituting the basis for the organization\u2019s exemption, and (ii) in the case of a contribution of food, such food is to be used by the organization to carry out such purpose or function. (2) Certain transportation costs included Such term shall include an amount to account for the use of a vehicle in the course of delivering a qualified charitable donation of food. Such amount shall not exceed the standard mileage rate in effect under section 170(i) with respect to such use. (c) Special rules For purposes of this section\u2014 (1) Denial of double benefit In the case of a taxpayer who elects the application of this section, no amount taken into account in determining the credit allowed under this section shall be taken into account in determining any deduction or other credit allowed under this chapter. (2) Carryforward (A) In general If the credit allowable under subsection (a) (and to which subsection (d)(2) applies) for any taxable year exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under subpart A (other than this section and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such taxable year. (B) Limitation No credit may be carried forward under this subsection to any taxable year following the fifth taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in first-out basis. (3) Substantiation requirements Rules similar to the rules of section 170(f)(8) shall apply for purposes of contributions taken into account under this section. (d) Application with other credits (1) Business credit treated as part of general business credit So much of the credit which would be allowed as a credit under subsection (a) for any taxable year (determined without regard to this subsection) that is attributable to cash or food from any trade or business of the taxpayer shall be treated as a credit listed in section 38(b) for such taxable year (and not allowed under subsection (a)). (2) Personal credit For purposes of this title, the credit allowed under subsection (a) for any taxable year (determined after the application of paragraph (1)) shall be treated as a credit allowed under subpart A for such taxable year. .\n##### (b) Portion of credit made part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the portion of the credit allowed under section 30E to which subsection (d)(1) thereof applies. .\n##### (c) Conforming amendment\nSection 23(c)(1) of such Code is amended by striking and section 25D and inserting and sections 25D and 30E .\n##### (d) Clerical amendment\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\nSec. 30E. Donations to charitable organizations that feed ill, needy, or infants. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-10-21",
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
        "name": "Taxation",
        "updateDate": "2025-11-20T17:59:33Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5809ih.xml"
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
      "title": "Fight Hunger Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fight Hunger Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against tax for food donations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:24Z"
    }
  ]
}
```
