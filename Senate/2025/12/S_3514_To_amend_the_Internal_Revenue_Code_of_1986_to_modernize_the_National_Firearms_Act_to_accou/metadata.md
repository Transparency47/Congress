# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3514
- Title: Less Than Lethal Act
- Congress: 119
- Bill type: S
- Bill number: 3514
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-03-26T11:03:17Z
- Update date including text: 2026-03-26T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8782)
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8782)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3514",
    "number": "3514",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Less Than Lethal Act",
    "type": "S",
    "updateDate": "2026-03-26T11:03:17Z",
    "updateDateIncludingText": "2026-03-26T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S8782)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
        "item": [
          {
            "date": "2025-12-16T23:06:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-16T23:06:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "WY"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "WV"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3514is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3514\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Barrasso introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modernize the National Firearms Act to account for advancements in technology and less-than-lethal weapons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Less Than Lethal Act .\n#### 2. Exemption of certain less-than-lethal projectile devices from firearms and ammunition tax\n##### (a) In general\nSection 4182 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e), and\n**(2)**\nby inserting after subsection (c) the following new subsection:\n(d) Less-Than-Lethal projectile devices (1) In general The tax imposed by section 4181 shall not apply to\u2014 (A) any less-than-lethal projectile device, (B) any device contained on the most recent list made available by the Secretary under paragraph (3)(B), and (C) any shell or cartridge that meets the requirement of paragraph (2)(B) and is designed for use in a device referred to in subparagraph (A) or (B). (2) Less-than-lethal projectile device The term less-than-lethal projectile device means a device that\u2014 (A) is not designed or intended to expel, and may not be readily converted to accept and discharge\u2014 (i) ammunition commonly used in handguns, rifles, or shotguns, or (ii) any other projectile at a velocity exceeding 500 feet per second, (B) is designed and intended to be used in a manner that is not likely to cause death or serious bodily injury, and (C) does not accept, and is not able to be readily modified to accept, ammunition feeding devices\u2014 (i) loaded through the inside of a pistol grip, or (ii) commonly used in semiautomatic firearms. (3) Request for classification Pursuant to a request made by the manufacturer, producer, or importer of a device for a determination as to whether such device satisfies the requirements under paragraph (2), the Secretary shall make such determination not later than 90 days after the date of receipt of such request. (4) Annual review of new and emerging technologies (A) List of less-than-lethal projectile devices The Secretary shall make publicly available a list of devices that the Secretary has determined are described in paragraph (2) and shall update such list annually to take into account new devices. (B) List of non-lethal devices the projectiles of which exceed 500 feet per second (i) In general The Secretary shall\u2014 (I) make publicly available a list of devices that the Secretary has determined are not described in paragraph (2) but would be so described if such paragraph were applied without regard to subparagraph (A)(ii) thereof, and (II) update such list annually to take into account new devices. (ii) Report to Congress The Secretary shall annually submit a written report to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate regarding the annual list of devices described in clause (i), including a copy of such list, a description of the devices that were considered for inclusion on such list, and the reasons for including or excluding such devices from such list. .\n##### (b) Effective date\nThe amendments made by this section shall apply to articles sold by the manufacturer, producer, or importer after the date of the enactment of this Act.\n#### 3. Exemption of certain less-than-lethal projectile devices from National Firearms Act\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking an antique firearm or and inserting any antique firearm, any less-than-lethal projectile device (as defined in section 4182(d)(2)), any device referred to in section 4182(d)(1)(B), or .",
      "versionDate": "2025-12-16",
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
        "actionDate": "2026-02-02",
        "text": "Placed on the Union Calendar, Calendar No. 407."
      },
      "number": "4242",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Innovate Less Lethal to De-Escalate Tax Modernization Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Firearms and explosives",
            "updateDate": "2026-01-20T19:46:17Z"
          },
          {
            "name": "Sales and excise taxes",
            "updateDate": "2026-01-20T19:46:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2026-01-12T22:29:08Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3514is.xml"
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
      "title": "Less Than Lethal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Less Than Lethal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:24:10Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modernize the National Firearms Act to account for advancements in technology and less-than-lethal weapons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:18:34Z"
    }
  ]
}
```
