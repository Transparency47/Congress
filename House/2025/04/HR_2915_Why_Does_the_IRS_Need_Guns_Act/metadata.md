# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2915?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2915
- Title: Why Does the IRS Need Guns Act
- Congress: 119
- Bill type: HR
- Bill number: 2915
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2025-12-05T22:04:36Z
- Update date including text: 2025-12-05T22:04:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2915",
    "number": "2915",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Why Does the IRS Need Guns Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:04:36Z",
    "updateDateIncludingText": "2025-12-05T22:04:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
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
          "date": "2025-04-14T13:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-14T13:00:15Z",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "WY"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "LA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2915ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2915\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Mr. Moore of Alabama (for himself, Ms. Hageman , Mr. Higgins of Louisiana , and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the Internal Revenue Service from providing firearms and ammunition to its employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Why Does the IRS Need Guns Act .\n#### 2. Definitions\nFor purposes of this Act:\n**(1) Ammunition**\nThe term ammunition has the same meaning given such term under section 921(a)(17) of title 18, United States Code.\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Internal Revenue.\n**(3) Firearm**\nThe term firearm has the same meaning given such term under section 921(a)(3) of title 18, United States Code.\n#### 3. Prohibition on use of funds\n##### (a) In general\nNotwithstanding any other provision of law, none of the funds authorized to be appropriated or otherwise made available for any fiscal year may be obligated or expended by the Commissioner to purchase, receive, or store any firearm or ammunition.\n##### (b) Effective date\nThis section shall take effect on the date which is 120 days after the date of enactment of this Act.\n#### 4. Transfer of firearms and ammunition\nNot later than the date which is 120 days after the date of enactment of this Act, the Commissioner shall transfer to the Administrator of General Services\u2014\n**(1)**\nany firearms owned by, or under the control of, the Internal Revenue Service; and\n**(2)**\nany ammunition owned by, or under the control of, the Internal Revenue Service.\n#### 5. Sale of firearms\n##### (a) In general\nNot later than the date which is 30 days after the date on which the transfer described in section 4 has been completed, the Administrator of General Services shall\u2014\n**(1)**\ninitiate the sale or auction of any firearms described in paragraph (1) of such section to licensed dealers (as defined in section 921(a)(11) of title 18, United States Code); and\n**(2)**\ninitiate the auction of any ammunition described in paragraph (2) of section 4 to members of the general public.\n##### (b) Proceeds\nAny proceeds from the sale or auction of property described in subsection (a) shall be deposited in the general fund of the Treasury for the sole purpose of deficit reduction.\n#### 6. Administration of criminal investigations by Attorney General\n##### (a) In general\nWith respect to the administration and enforcement of\u2014\n**(1)**\nany of the criminal provisions of the internal revenue laws,\n**(2)**\nany other criminal provisions of law relating to internal revenue for the enforcement of which the Secretary of the Treasury, as of the date of enactment of this Act, was responsible, or\n**(3)**\nany other law for which the Secretary of the Treasury, as of the date of enactment of this Act, delegated investigatory authority to the Internal Revenue Service,\nsuch administration and enforcement shall be performed by or under the supervision of the Attorney General.\n##### (b) Performance of transferred functions\nThe Attorney General may make such provisions as the Attorney General determines appropriate to authorize the performance by any officer, employee, or agency of the Department of Justice of any function transferred to the Attorney General under this section.\n##### (c) Transfer of authorities, functions, personnel, and assets to the Department of Justice\nNotwithstanding any other provision of law, there are transferred to the Department of Justice the authorities, functions, personnel, and assets of the Criminal Investigation Division of the Internal Revenue Service, which shall be maintained as a distinct entity within the Criminal Division of the Department of Justice, including the related functions of the Secretary of the Treasury.\n##### (d) Effective date\nThis section shall take effect on the date which is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-04-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1436",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Why Does the IRS Need Guns Act",
      "type": "S"
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
        "updateDate": "2025-05-28T15:13:03Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2915ih.xml"
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
      "title": "Why Does the IRS Need Guns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Why Does the IRS Need Guns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Internal Revenue Service from providing firearms and ammunition to its employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T06:48:23Z"
    }
  ]
}
```
