# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7790?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7790
- Title: Medical Records Access Fairness Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7790
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-27T16:41:24Z
- Update date including text: 2026-03-27T16:41:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7790",
    "number": "7790",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Medical Records Access Fairness Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-27T16:41:24Z",
    "updateDateIncludingText": "2026-03-27T16:41:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7790ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7790\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Foster (for himself and Mrs. Beatty ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the HITECH Act to allow an individual to obtain a copy of such individual\u2019s protected health information at no cost unless certain circumstances apply, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Records Access Fairness Act of 2026 .\n#### 2. Access of individuals to protected health information at no cost unless certain circumstances apply\nSection 13405 of the HITECH Act ( 42 U.S.C. 17935 ) is amended by adding at the end the following new subsection:\n(f) Access of individuals to protected health information at no cost unless certain circumstances apply (1) Access of individuals to protected health information at no cost unless certain circumstances apply (A) In general In providing an individual (and, if the individual expressly requests, a health care provider or a family caregiver) with access to a copy of such individual\u2019s protected health information (or a summary or explanation of such information) in accordance with section 164.524 of title 45, Code of Federal Regulations, a health care provider may only impose a fee on such individual if the individual is requesting\u2014 (i) a duplicate copy (or summary or explanation) of protected health information that was previously provided to such individual in the same calendar year of the request; or (ii) a non-electronic copy (or summary or explanation) of protected health information that the health care provider has made accessible for the individual, at no cost, on an online portal of the health care provider. (B) Copies transmitted to other health care providers In the case of an individual who expressly requests a health care provider to transmit to another health care provider a copy of such individual\u2019s protected health information (or a summary or explanation of such information), such transmitting provider may transmit such copy (or summary or explanation) in any form and format to the extent that such form and format is readily usable by such receiving provider. (C) Rule of construction Nothing in this subsection may be construed as requiring a health care provider to provide, at no cost, a copy of an individual\u2019s protected health information (or a summary or explanation of such information) to any attorney of such individual. (2) Regulations Not later than six months after the date of the enactment of this subsection, the Secretary of Health and Human Services shall promulgate and amend regulations as necessary to implement the requirements described in this subsection. (3) Effective date This subsection shall apply with respect to requests for access to protected health information made on or after the date that is 180 days after the date of the enactment of this subsection. .",
      "versionDate": "2026-03-04",
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
        "name": "Health",
        "updateDate": "2026-03-27T16:41:24Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7790ih.xml"
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
      "title": "Medical Records Access Fairness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-22T05:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Records Access Fairness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-22T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the HITECH Act to allow an individual to obtain a copy of such individual's protected health information at no cost unless certain circumstances apply, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-22T05:33:27Z"
    }
  ]
}
```
