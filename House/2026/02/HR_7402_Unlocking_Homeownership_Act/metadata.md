# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7402
- Title: Unlocking Homeownership Act
- Congress: 119
- Bill type: HR
- Bill number: 7402
- Origin chamber: House
- Introduced date: 2026-02-05
- Update date: 2026-04-21T08:06:01Z
- Update date including text: 2026-04-21T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-05: Introduced in House

## Actions

- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7402",
    "number": "7402",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Unlocking Homeownership Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:01Z",
    "updateDateIncludingText": "2026-04-21T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T15:02:30Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7402ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7402\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2026 Mr. Moore of North Carolina introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow distributions from qualified tuition programs for first home purchases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unlocking Homeownership Act .\n#### 2. Allowance of distributions from qualified tuition programs for first home purchases\n##### (a) In general\nSection 529(c)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(F) Distributions for first home purchases (i) In general Subparagraph (A) shall not apply to any qualified first-time homebuyer distribution. (ii) Qualified first-time homebuyer distribution For purposes of this subparagraph, the term qualified first-time homebuyer distribution means any distribution from a qualified tuition program of a designated beneficiary which is received by such beneficiary to the extent such distribution is used by the beneficiary before the close of the 120th day after the day on which such distribution is received to pay qualified acquisition costs with respect to a principal residence of a first-time homebuyer who is such beneficiary, the spouse of such beneficiary, or any child, grandchild, or ancestor of such beneficiary or the beneficiary\u2019s spouse. (iii) Qualified acquisition costs For purposes of this subparagraph, the term qualified acquisition costs has the meaning given that term in section 72(t)(8). (iv) First-time homebuyer; other definitions For purposes of this subparagraph\u2014 (I) First-time homebuyer The term first-time homebuyer means any individual if such individual (and if married, such individual\u2019s spouse) had no present ownership interest in a principal residence during the 2-year period ending on the date of acquisition of the principal residence to which clause (ii) applies. (II) Principal residence The term principal residence has the same meaning as when used in section 121. (III) Date of acquisition The term date of acquisition means the date on which a binding contract to acquire the principal residence to which clause (ii) applies is entered into, or on which construction or reconstruction of such a principal residence is commenced. (v) Special rule where delay in acquisition If any distribution from a qualified tuition program fails to meet the requirements of clause (ii) solely by reason of a delay or cancellation of the purchase or construction of the residence, the amount of the distribution may be transferred to another qualified tuition program of the designated beneficiary as provided in subparagraph (C)(i)(I), or an ABLE account of such beneficiary as provided in subparagraph (C)(i)(III), determined by substituting 120 days for 60 days in subparagraph (C)(i), except that\u2014 (I) subparagraph (C)(iii) shall not be applied to such transfer, and (II) such amount shall not be taken into account in determining whether subparagraph (C)(iii) applies to any other amount. (vi) Recontributions (I) General rule Any designated beneficiary who received a qualified distribution may, during the applicable period, make one or more contributions in an aggregate amount not to exceed the amount of such qualified distribution to any qualified tuition program or ABLE account of such beneficiary to which a transfer of such distribution could be made under subclause (I) or (III) of subparagraph (C)(i). (II) Treatment of repayments For purposes of this paragraph, if a contribution is made pursuant to subclause (I) with respect to a qualified distribution, then the designated beneficiary shall, to the extent of the amount of the contribution, be treated as having received the qualified distribution as a transfer under subparagraph (C)(i) within 60 days of the distribution. (III) Qualified distribution For purposes of this clause, the term qualified distribution means any distribution which is a qualified first-time homebuyer distribution, which was to be used to purchase or construct a principal residence in a qualified disaster area but was not so used on account of the qualified disaster with respect to such area, and which was received during the period beginning on the date which is 180 days before the first day of the incident period of such qualified disaster and ending on the date which is 30 days after the last day of such incident period. (IV) Applicable period For purposes of this clause, the term applicable period means, in the case of a principal residence in a qualified disaster area with respect to any qualified disaster, the period beginning on the first day of the incident period of such qualified disaster and ending on the date which is 180 days after the applicable date with respect to such disaster. (V) Qualified disaster For purposes of this clause, the term qualified disaster means any disaster with respect to which a major disaster has been declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act after the date of the enactment of this clause. (VI) Qualified disaster area For purposes of this clause, the term qualified disaster area means, with respect to any qualified disaster, the area with respect to which the major disaster was declared under the Robert T. Stafford Disaster Relief and Emergency Assistance Act. (VII) Incident period For purposes of this clause, the term incident period means, with respect to any qualified disaster, the period specified by the Federal Emergency Management Agency as the period during which such disaster occurred. (VIII) Applicable date For purposes of this clause, the term applicable date means the latest of the date of the enactment of this subparagraph, the first day of the incident period with respect to the qualified disaster, or the date of the disaster declaration with respect to the qualified disaster. .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.",
      "versionDate": "2026-02-05",
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
        "updateDate": "2026-02-23T16:28:43Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7402ih.xml"
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
      "title": "Unlocking Homeownership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unlocking Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow distributions from qualified tuition programs for first home purchases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T10:48:22Z"
    }
  ]
}
```
