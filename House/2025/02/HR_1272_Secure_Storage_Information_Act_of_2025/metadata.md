# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1272
- Title: Secure Storage Information Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1272
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-05-06T13:29:46Z
- Update date including text: 2025-05-06T13:29:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1272",
    "number": "1272",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Secure Storage Information Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-06T13:29:46Z",
    "updateDateIncludingText": "2025-05-06T13:29:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-12T15:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1272ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1272\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Sherrill (for herself, Ms. Williams of Georgia , Ms. Brownley , Ms. Stevens , Ms. Norton , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 18, United States Code, to require a Federal firearms licensee to provide secure firearms storage information to a prospective firearm transferee, and to amend the Internal Revenue Code of 1986 to provide a gun safe credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Storage Information Act of 2025 .\n#### 2. Requirement that a Federal firearms licensee provide secure firearms storage information to a prospective firearm transferee\n##### (a) In general\nSection 922(z) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking (1) In general.\u2014 Except and inserting the following:\n(1) Requirement that device be provided with handgun (A) In general Except ;\n**(B)**\nby adding after and below the end the following:\n(B) Requirement to provide secure storage information with any firearm It shall be unlawful for any licensed importer, licensed manufacturer, or licensed dealer to sell, deliver, or transfer a firearm to any person other than a person licensed under this chapter, unless the transferee is provided with such information about the secure storage of firearms as the Attorney General shall prescribe. ; and\n**(2)**\nin paragraph (2), by striking (1) and inserting (1)(A) .\n##### (b) Regulations\nWithin 6 months after the date of the enactment of this Act, the Attorney General shall prescribe, by regulation, the secure firearms storage information required to be provided by a Federal firearms licensee to a prospective firearm transferee, and ensure that the information includes\u2014\n**(1)**\nthat firearms should be stored unloaded, out of the reach of children and other persons without authorized access, and separately from ammunition;\n**(2)**\nthat stored firearms should be secured with a locking device;\n**(3)**\na statement as to the importance of secure storage, including data on the risks of unsecured firearms and benefits of securely stored firearms in relation to firearm suicide, firearm homicide and assault, school firearm violence, unintentional shootings, and theft; and\n**(4)**\nguidance on the most secure types of devices, including the advantages of gun safes and lock boxes compared to trigger and cable locks.\n#### 3. Requirement that certain Federal firearms licensees have a variety of secure gun storage or safety devices available for purchase in their stores\nSection 923 of title 18, United States Code, is amended in each of subsections (d)(1)(G) and (e)\u2014\n**(1)**\nby striking secure gun storage or safety devices and inserting a variety of secure gun storage or safety devices, including full-size gun safes, lock boxes and lockers, gun cases, or cable and trigger locks, ;\n**(2)**\nby striking a secure gun storage or safety device and inserting secure gun storage or safety devices ; and\n**(3)**\nby striking a device and inserting devices .\n#### 4. Effective date\nThe amendments made by sections 2 and 3 shall take effect on the date that is 6 months after the date of the enactment of this Act.\n#### 5. Gun safe credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 26 the following new section:\n25F. Gun safe credit (a) In general In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the amounts paid or incurred by the taxpayer for the taxable year for the purchase of a qualified gun safe. (b) Limitation The credit allowed under this section with respect to any taxpayer for any taxable year shall not exceed the excess (if any) of $500 over the aggregate credits allowed under this section with respect to such taxpayer for all prior taxable years. (c) Qualified gun safe For purposes of this section, the term qualified gun safe means any safe, gun safe, gun case, lock box, or other device\u2014 (1) the original use of which commences with the taxpayer, (2) which is acquired by the taxpayer\u2014 (A) to store one or more firearms, and (B) not for resale, (3) which is designed, or can be used, for the secure and fully-contained storage of one or more firearms, and (4) which is designed to be unlocked only by authorized users by means of a key, a combination, biometric credentials, or other similar means. (d) Reduction in basis For purposes of this subtitle, the basis of any property for which a credit is allowable under subsection (a) shall be reduced by the amount of such credit so allowed. (e) No double benefit The amount of any deduction allowable under this chapter with respect to a property for which a credit is allowable under subsection (a) shall be reduced by the amount of such credit so allowed. .\n##### (b) Conforming amendment\nSection 1016(a) of such Code is amended by striking and at the end of paragraph (37), by striking the period at the end of paragraph (38) and inserting , and , and by adding at the end the following new paragraph:\n(39) to the extent provided in section 25F(d). .\n##### (c) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting before the item relating to section 26 the following new item:\nSec. 25F. Gun safe credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-12",
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
        "updateDate": "2025-05-06T13:29:46Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1272ih.xml"
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
      "title": "Secure Storage Information Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Storage Information Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to require a Federal firearms licensee to provide secure firearms storage information to a prospective firearm transferee, and to amend the Internal Revenue Code of 1986 to provide a gun safe credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T15:18:31Z"
    }
  ]
}
```
