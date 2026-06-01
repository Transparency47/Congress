# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8021
- Title: American Petroleum First Act
- Congress: 119
- Bill type: HR
- Bill number: 8021
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-03T21:43:06Z
- Update date including text: 2026-04-03T21:43:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8021",
    "number": "8021",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "American Petroleum First Act",
    "type": "HR",
    "updateDate": "2026-04-03T21:43:06Z",
    "updateDateIncludingText": "2026-04-03T21:43:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "OH"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8021ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8021\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Perry (for himself, Mr. Roy , and Mr. Davidson ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo exempt certain vessels transporting crude oil and petroleum products from certain coastwise endorsement requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Petroleum First Act .\n#### 2. Exemption from coastwise laws for vessels transporting crude oil and petroleum products\n##### (a) General eligibility requirements\nSection 12103 of title 46, United States Code, is amended by adding at the end the following:\n(d) Exception for vessels transporting crude oil and petroleum products (1) In general Notwithstanding subsection (a), a certificate of documentation may be issued under this chapter for any vessel transporting crude oil and petroleum products. (2) Certain vessels excluded Paragraph (1) shall not apply to\u2014 (A) a vessel that is owned, in whole or in part, by\u2014 (i) a Russian national; or (ii) the Government of the Russian Federation; and (B) a Russian-flagged vessel; (C) a vessel for which any crewmember is a Russian national; (D) a vessel that is owned, in whole or in part, by\u2014 (i) a Chinese national; or (ii) the People\u2019s Republic of China; (E) a Chinese-flagged vessel; or (F) a vessel for which any crewmember is a Chinese national. .\n##### (b) Coastwise endorsement\nSection 12112(a)(2)(B) of title 46, United States Code, is amended\u2014\n**(1)**\nin clause (ii) by striking or at the end;\n**(2)**\nin clause (iii) by striking and at the end and inserting or ; and\n**(3)**\nby adding at the end the following:\n(iv) transports crude oil and petroleum products; and .",
      "versionDate": "2026-03-19",
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
        "name": "Energy",
        "updateDate": "2026-04-03T21:43:06Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8021ih.xml"
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
      "title": "American Petroleum First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T12:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Petroleum First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt certain vessels transporting crude oil and petroleum products from certain coastwise endorsement requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T12:03:26Z"
    }
  ]
}
```
