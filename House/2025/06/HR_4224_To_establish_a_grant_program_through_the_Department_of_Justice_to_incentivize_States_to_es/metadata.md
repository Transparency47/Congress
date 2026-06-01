# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4224?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4224
- Title: Background Check Point of Contact Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4224
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-07-28T12:45:53Z
- Update date including text: 2025-07-28T12:45:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4224",
    "number": "4224",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Background Check Point of Contact Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-28T12:45:53Z",
    "updateDateIncludingText": "2025-07-28T12:45:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:04:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4224ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4224\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Ms. Dean of Pennsylvania introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program through the Department of Justice to incentivize States to establish point-of-contact systems for firearm sales subject to a background check, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Background Check Point of Contact Act of 2025 .\n#### 2. Grants established\n##### (a) In general\n**(1) Establishment**\nThe Attorney General may make an annual grant of not more than $1,000,000 to each eligible State that has conformed to the requirements of this Act. Such grant may be renewed for each year that the State remains in such conformity. The grant shall be used for the establishment, operation, and maintenance of a point-of-contact system as set forth in section 3.\n**(2) Authorization of appropriations**\nThere are authorized to carry out this program not more than $10,000,000 each fiscal year.\n**(3) Matching requirement**\nThe Federal share of the cost of a point-of-contact system carried out using grant funds may not exceed 25 percent.\n##### (b) Preference for other grants\nThe Attorney General shall give preference in awards of any discretionary grant administered by the Bureau of Justice Assistance to a State that has conformed its laws in accordance with this Act.\n#### 3. Point-of-contact systems required\nTo be in compliance with this section, a State shall conform its laws to the following:\n**(1)**\nA point-of-contact system for the sale or transfer of a firearm shall be established or maintained, under which a person licensed under section 923 of title 18, United States Code, may verify that the sale or transfer would be lawful.\n**(2)**\nA sale or transfer of a firearm may not be completed unless the parties to the sale or transfer receive an approval number issued by the point-of-contact system not later than 10 days after the sale or transfer is initiated.\n**(3)**\nThe point-of-contact system may not issue an approval number if the system cannot confirm that the sale or transfer would be lawful.\n**(4)**\nA hotline shall be established, to be operated by the State, to be used by a person licensed under section 923 of title 18, United States Code, for purposes of contacting the national instant criminal background check system.\n**(5)**\nA fund shall be established by the State for the operation of the point-of-contact system.\n**(6)**\nAn appeals process in the case of any failure by the point-of-contact system to issue an approval number, with the burden of proof on the State to prove that there was a valid basis for failure to issue shall be established.\n**(7)**\nFor each denial, the information will be transferred to the state or local law enforcement agency responsible for investigating the denial as a violation of law.\n#### 4. Reporting requirement\nTo be in compliance with this section, a State that receives a grant under this Act shall publish an annual report that contains information substantially similar to the information included in a NICS operations report made by the Director of the Federal Bureau of Investigation and additionally includes the following:\n**(1)**\nThe number of investigations resulting from failures to issue approval numbers.\n**(2)**\nResults of investigations reported.\n**(3)**\nDenied appeals that were overturned.\n**(4)**\nTotal number of hours where point of contact system was not functional resulting in a halt in processing checks.\n**(5)**\nThe number of persons arrestsed as a result of an information transfer under section 3(7).\n#### 5. Annual audit\nTo be in compliance with this section, a State shall submit to an annual audit by the Director of the Federal Bureau of Investigation of the point-of-contact system established under section 3.\n#### 6. Definitions\nIn this Act:\n**(1)**\nThe term firearm has the meaning given such term in section 921 of title 18, United States Code.\n**(2)**\nThe terms law enforcement agency and unit of local government have the meanings given such terms in section 901 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n**(3)**\nThe term State includes each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, and any other territory of the United States.",
      "versionDate": "2025-06-27",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-28T12:45:53Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4224ih.xml"
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
      "title": "Background Check Point of Contact Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Background Check Point of Contact Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program through the Department of Justice to incentivize States to establish point-of-contact systems for firearm sales subject to a background check, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T04:18:29Z"
    }
  ]
}
```
