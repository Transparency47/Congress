# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8753
- Title: Gas Tax Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 8753
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-27T08:23:30Z
- Update date including text: 2026-05-27T08:23:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8753",
    "number": "8753",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Gas Tax Relief Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:23:30Z",
    "updateDateIncludingText": "2026-05-27T08:23:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:05:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8753ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8753\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Ms. Malliotakis (for herself and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax holiday for gasoline and diesel fuel.\n#### 1. Short title\nThis Act may be cited as the Gas Tax Relief Act .\n#### 2. 2026 tax holiday for taxable fuels\n##### (a) In general\nIn the case of taxable fuel (as defined in section 4083(a)(1) of the Internal Revenue Code of 1986) removed, entered, or sold on or after the date of the enactment of this Act and before the applicable date\u2014\n**(1)**\nthe rate of tax under clauses (i) and (iii) of section 4081(a)(2)(A) of the Internal Revenue Code of 1986 shall be zero, and\n**(2)**\nthe Leaking Underground Storage Tank Trust Fund financing rate under section 4081(a)(2)(B) of such Code shall not apply to taxable fuel to which the rate under paragraph (1) applies.\n##### (b) Transfers to Trust Fund\n**(1) In general**\nThe Secretary of the Treasury shall transfer from the general fund to the Highway Trust Fund established under section 9503(a) of the Internal Revenue Code of 1986 and the Leaking Underground Storage Tank Trust Fund established under section 9508(a) of such Code amounts equal to the reduction in amounts credited (but for this subsection) to each such Trust Fund by reason of subsection (a).\n**(2) Coordination rules**\n**(A) Leaking Underground Storage Tank Trust Fund**\nAmounts transferred to the Leaking Underground Storage Tank Trust Fund under paragraph (1) shall be treated for purposes of sections 9503(b)(1) and 9508(b)(2) of such Code as taxes received in the Treasury under section 4081 of such Code attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n**(B) Highway Trust Fund**\nAmounts transferred to the Highway Trust Fund under paragraph (1) shall be treated for purposes of section 9503(b)(1) of such Code as taxes received in the Treasury under section 4081 of such Code which are not attributable to the Leaking Underground Storage Tank Trust Fund financing rate.\n##### (c) Applicable date\nFor purposes of this section, the term applicable date means\u2014\n**(1)**\nthe date which is 90 days after the date of enactment of this Act,\n**(2)**\nif the President determines, in the President's sole discretion, that economic conditions merit an additional suspension of the tax on taxable fuels described in subsection (a), the date that is 215 days after the date of enactment of this Act, and\n**(3)**\nif the President determines that a phased-in reimplementation of the tax on taxable fuels described in subsection (a) is appropriate, the President may provide for such phased-in reimplementation through incremental restoration of the rates otherwise applicable under section 4081 beginning on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8753ih.xml"
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
      "title": "Gas Tax Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gas Tax Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a tax holiday for gasoline and diesel fuel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:18:40Z"
    }
  ]
}
```
