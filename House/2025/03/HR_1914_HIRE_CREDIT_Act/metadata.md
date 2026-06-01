# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1914?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1914
- Title: HIRE CREDIT Act
- Congress: 119
- Bill type: HR
- Bill number: 1914
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-08T14:02:06Z
- Update date including text: 2025-05-08T14:02:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1914",
    "number": "1914",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "HIRE CREDIT Act",
    "type": "HR",
    "updateDate": "2025-05-08T14:02:06Z",
    "updateDateIncludingText": "2025-05-08T14:02:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:01:35Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1914ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1914\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Ms. Crockett (for herself, Mr. Edwards , Ms. Chu , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow the work opportunity tax credit for hiring displaced disaster victims.\n#### 1. Short title\nThis Act may be cited as the Helping Increase Realtime Employment for Communities Recovering from Emergency Disasters for an Interim Time Act or as the HIRE CREDIT Act .\n#### 2. Work opportunity tax credit for hiring displaced disaster victims\n##### (a) In general\nSection 51(d) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (I), by striking the period at the end of subparagraph (J) and inserting , or , and by adding at the end the following new subparagraph:\n(K) a displaced disaster victim. .\n##### (b) Displaced disaster victim\nSection 51(d) of such Code is amended by adding at the end the following new paragraph:\n(16) Displaced disaster victim (A) In general The term displaced disaster victim means any individual who is certified by the designated local agency\u2014 (i) as having a principal residence (as defined in section 1033(h)(4)) in a qualified disaster zone which was rendered uninhabitable as a result of the qualified disaster with respect to such qualified disaster zone, (ii) as being employed (immediately prior to the incident period with respect to such qualified disaster) at a location in such qualified disaster zone which was rendered inoperable as a result of such qualified disaster, and (iii) as being in a period of unemployment. (B) Temporary status The term displaced disaster victim shall not include any individual unless the hiring date with respect to such individual is before the date which is 1 year after the last day of the incident period with respect to the qualified disaster referred to in subparagraph (A). (C) Exclusion of full-time employment outside of qualified disaster zone If the principal place of employment by the taxpayer of any displaced disaster victim is outside of the qualified disaster zone with respect to such individual, the term qualified wages shall not include any amount paid or incurred by such employer as compensation for the services of such individual with respect any calendar week if such individual provided 30 or more hours of services to such employer during such week. (D) Qualified disaster zone The term qualified disaster zone means any area\u2014 (i) with respect to which a major disaster was declared, on or after January 1, 2024, by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act, and (ii) which was determined by the President, on or after January 1, 2024, to warrant individual or individual and public assistance from the Federal Government under the Robert T. Stafford Disaster Relief and Emergency Assistance Act by reason of the qualified disaster with respect to such disaster area. (E) Qualified disaster The term qualified disaster means, with respect to any qualified disaster zone, the disaster by reason of which a major disaster was declared with respect to such area. (F) Incident period The term incident period means, with respect to any qualified disaster, the period specified by the Federal Emergency Management Agency as the period during which such disaster occurred (except that for purposes of this paragraph such period shall not be treated as beginning before January 1, 2024). .\n##### (c) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer on or after January 1, 2024.\n##### (d) Transition rules\nIn the case of any qualified disaster the incident period of which ends before the date of the enactment of this Act\u2014\n**(1)**\nsection 51(d)(16)(B) of the Internal Revenue Code of 1986 shall be applied by substituting the date of the enactment of this Act for the last day and all that follows, and\n**(2)**\nin the case of an individual who begins work for the employer before the date of the enactment of this Act, section 51(d)(15)(A)(iii) shall be determined with respect to the period before the date on which such individual so begins such work.",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-05-08T14:02:06Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1914ih.xml"
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
      "title": "HIRE CREDIT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HIRE CREDIT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Increase Realtime Employment for Communities Recovering from Emergency Disasters for an Interim Time Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow the work opportunity tax credit for hiring displaced disaster victims.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:37Z"
    }
  ]
}
```
