# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8619?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8619
- Title: Kimberly Vaughan Firearm Safe Storage Act
- Congress: 119
- Bill type: HR
- Bill number: 8619
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T08:08:31Z
- Update date including text: 2026-05-20T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H3541)
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H3541)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8619",
    "number": "8619",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001245",
        "district": "18",
        "firstName": "Christian",
        "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
        "lastName": "Menefee",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Kimberly Vaughan Firearm Safe Storage Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:31Z",
    "updateDateIncludingText": "2026-05-20T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3541)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:05:50Z",
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
          "date": "2026-04-30T13:05:45Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8619ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8619\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Menefee introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo make unlawful the sale of any firearm by a licensed manufacturer, licensed importer, or licensed dealer without a written notice promoting safe storage and a safe storage device, to create and disseminate best practices regarding safe firearm storage, to create a grant program for the distribution of safe storage devices, and to amend the Internal Revenue Code of 1986 to allow for a credit against tax for sales at retail of safe firearm storage devices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kimberly Vaughan Firearm Safe Storage Act .\n#### 2. Best practices for safe firearm storage\n##### (a) Establishment\n**(1) In general**\n**(A)**\nNot later than 180 days after the enactment of this Act, the Attorney General shall establish voluntary best practices relating to safe firearm storage solely for the purpose of public education.\n**(B)**\nThe Attorney General shall give not less than ninety days public notice, and shall afford interested parties opportunity for hearing, before establishing such best practices.\n**(2) Requirements**\nIn establishing the best practices required under paragraph (1), the Attorney General shall outline such best practices for preventing firearm loss, theft, and other unauthorized access for the following locations:\n**(A)**\nBusinesses.\n**(B)**\nVehicles.\n**(C)**\nPrivate homes.\n**(D)**\nOff-site storage facilities.\n**(E)**\nAny other such place the Attorney General deems appropriate to provide such guidance.\n**(3) Publication**\nNot later than 1 year after the enactment of this Act, the Attorney General shall publish, in print and on a public website, the best practices created pursuant to paragraph (1) and shall review such best practices and update them not less than annually.\n#### 3. Promotion of safe firearm storage\n##### (a) In general\nSection 923 of title 18, United States Code, is amended by adding at the end the following:\n(m) Beginning on January 1, 2029, licensed manufacturers and licensed importers that serialize not less than 250 firearms annually pursuant to subsection (i) shall provide a clear and conspicuous written notice with each manufactured or imported handgun, rifle, or shotgun that\u2014 (1) is attached or adhered to, or appears on or within any packaging of, each handgun, rifle, or shotgun; and (2) states SAFE STORAGE SAVES LIVES followed by the address of the public website established by the Attorney General pursuant to section 2 of the Kimberly Vaughan Firearm Safe Storage Act. .\n#### 4. Safe storage devices for all firearm sales\n##### (a) In general\nSection 922(z) of title 18, United States Code, is amended by striking handgun each place it appears and inserting handgun, rifle, or shotgun .\n##### (b) Effective date\nThis section and the amendments made by this section shall take effect on the date that is 180 days after the enactment of this Act.\n#### 5. Safe firearm storage grant program\n##### (a) In general\nThe Attorney General may award grants to States and Indian Tribes for the development, implementation, and evaluation of Safe Firearm Storage Assistance Programs.\n##### (b) Definitions\nFor purposes of this section:\n**(1)**\nThe term safe firearm storage device means a device that is\u2014\n**(A)**\ndesigned and marketed for the principal purpose of denying unauthorized access to, or rendering inoperable, a firearm or ammunition; and\n**(B)**\nsecured by a combination lock, key lock, or lock based on biometric information which, once locked, is incapable of being opened without the combination, key, or biometric information, respectively.\n**(2)**\nThe term Safe Firearm Storage Assistance Program means a program\u2014\n**(A)**\ncarried out by a unit of local government or an Indian tribe; and\n**(B)**\nsolely for the purpose of acquiring and distributing safe firearm storage devices to the public.\n##### (c) Application requirements\nEach applicant for a grant under this section shall\u2014\n**(1)**\nsubmit to the Attorney General an application at such time, in such a manner, and containing such information as the Attorney General may require; and\n**(2)**\nto the extent practicable, identify State, local, Tribal, and private funds available to supplement the funds received under this section.\n##### (d) Reporting requirement\n**(1) Grantee report**\nA recipient of a grant under this section shall submit to the Attorney General an annual report, which includes the following information:\n**(A)**\nThe amount distributed to each Safe Firearm Storage Assistance Program in the jurisdiction.\n**(B)**\nThe number of safe firearm storage devices distributed by each such Safe Firearm Storage Assitance Program.\nA recipient of a grant under this section may not include any personally identifying information of recipients of safe firearms storage devices pursuant to a Safe Firearm Storage Assistance Program that received funding pursuant to this section.\n**(2) Attorney General report**\nBeginning 13 months after the first grants are awarded under this section, and annually thereafter, the Attorney General shall submit to Congress a report, which shall include the following information:\n**(A)**\nA list of grant recipients during the previous year, including the funds awarded, cumulatively and disaggregated by grantee.\n**(B)**\nThe information collected pursuant to subsection (d)(1).\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Attorney General to carry out this section $10,000,000 for each of fiscal years 2027 through 2037, to remain available until expended.\n##### (f) Use of funds\nFunds awarded under this section shall be allocated as follows:\n**(1)**\nNot less than 75 percent of the funds received by a grantee shall be used to create or to provide resources for Safe Firearm Storage Assistance Programs in the jurisdiction.\n**(2)**\nNot more than 25 percent of the funds received by a grantee may be made available to nonprofit organizations to partner with units of local government to purchase and distribute safe firearm storage devices.\n#### 6. Prevent family fire safe firearm storage credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Safe firearm storage credit (a) Allowance of credit For purposes of section 38, the safe firearm storage credit determined under this section for the taxable year is an amount equal to 10 percent of amounts received from the first retail sale of a safe firearm storage device for use within the United States. (b) Limitation (1) In general The amount taken into account under subsection (a) with respect to a safe firearm storage device shall not exceed $400. (2) Value If, in connection with a sale of a safe firearm storage device, the transferee receives other property, the amount taken into account under subsection (a) shall be limited to the amount received solely with respect to the safe firearm storage device, which shall be determined based on the value of the safe firearm storage device relative to the value of such other property. (c) Safe firearm storage device For purposes of this section\u2014 (1) In general The term safe firearm storage device means a device that is\u2014 (A) designed and marketed for the principal purpose of denying unauthorized access to, or rendering inoperable, a firearm or ammunition, and (B) secured by a combination lock, key lock, or lock based on biometric information which, once locked, is incapable of being opened without the combination, key, or biometric information, respectively. (2) Exclusion The term safe firearm storage device does not include\u2014 (A) any device which is incorporated to any extent into the design of a firearm or of ammunition, or (B) any device that, as of the day of the sale described in subsection (a), has been subject to a mandatory recall by the Consumer Product Safety Commission. (3) Firearm; ammunition The terms firearm and ammunition have the meanings given such terms in section 921(a) of title 18, United States Code (without regard to all that follows firearm silencer in paragraph (3) of such section). (d) Termination This section shall not apply to sales after December 31, 2035. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the safe firearm storage credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Safe firearm storage credit. .\n##### (d) Report\nThe Secretary of the Treasury shall make publicly available an annual report of the total amount of credit against tax determined under section 45BB of the Internal Revenue Code of 1986 for taxable years ending in the preceding calendar year, disaggregated by State.\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 7. Severability\nIf any provision of this Act, or an amendment made by this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act, or an amendment made by this Act, or the application of such provision to other persons or circumstances, shall not be affected.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4487",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gun Safety Incentive Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-15T15:30:59Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8619ih.xml"
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
      "title": "Kimberly Vaughan Firearm Safe Storage Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-02T03:38:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kimberly Vaughan Firearm Safe Storage Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-02T03:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make unlawful the sale of any firearm by a licensed manufacturer, licensed importer, or licensed dealer without a written notice promoting safe storage and a safe storage device, to create and disseminate best practices regarding safe firearm storage, to create a grant program for the distribution of safe storage devices, and to amend the Internal Revenue Code of 1986 to allow for a credit against tax for sales at retail of safe firearm storage devices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:35Z"
    }
  ]
}
```
