# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2325
- Title: CEMAC Act
- Congress: 119
- Bill type: HR
- Bill number: 2325
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-05-14T12:57:51Z
- Update date including text: 2025-05-14T12:57:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2325",
    "number": "2325",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "CEMAC Act",
    "type": "HR",
    "updateDate": "2025-05-14T12:57:51Z",
    "updateDateIncludingText": "2025-05-14T12:57:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2325ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2325\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Huizenga (for himself and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo withhold United States support for any action in the International Monetary Fund relating to member states of the Central African Economic Monetary Community until a determination as to gross foreign exchange reserves is made.\n#### 1. Short title\nThis Act may be cited as the Central African Exploitation and Manipulation of American Companies Act or the CEMAC Act .\n#### 2. Findings\nThe Congress finds as follows:\n**(1)**\nThe member states of the Central African Economic Monetary Community (CEMAC) hold significant oil and gas reserves and have enjoyed decades long relationships and investments with international oil companies (IOCs).\n**(2)**\nIn 2018, the central bank for CEMAC, the Bank of Central African States (BEAC) introduced and intended to enact a foreign exchange regulation that mandates extractive industry companies repatriate restoration funds for site rehabilitation to the BEAC.\n**(3)**\nSignificant progress has been made in mediated dialogues over the last 7 years to rectify 23 issues with this regulation raised by the IOCs. However, significant issues remain including the refusal of BEAC to remove its sovereign immunity from execution, the role of BEAC as custodian of restoration fund accounts, and the implementation of double jeopardy and material adverse change clauses.\n**(4)**\nBEAC has imposed a completely arbitrary deadline of April 30, 2025, for the IOCs to sign this agreement with penalties equivalent to 150 percent of the restoration fund starting May 1, 2025.\n**(5)**\nImplementation of this regulation is expected to create a lasting negative impact on oil and gas investment in the Central African region, and will drastically compound an already challenging investment environment.\n**(6)**\nThe member states of BEAC have indicated that these restoration funds will help them shore up their foreign exchange reserves, despite restoration funds being exclusively allocated for restoration work costs and therefore not meeting the criteria of the International Monetary Fund (IMF) for foreign exchange reserves.\n**(7)**\nThe IMF\u2019s Balance of Payments and International Investment Position Manual states that assets must be readily available and controlled by a country\u2019s monetary authorities to count towards a country\u2019s foreign exchange reserves.\n**(8)**\nOil and gas investments in the CEMAC region have been declining since 2018 and this BEAC foreign exchange regulation is expected to drastically accelerate this decline.\n**(9)**\nStandard & Poor\u2019s estimates that the regulation by 2050 will result in a reduction of government revenue for CEMAC member states of $86,000,000,000, and a reduction in capital investment of $45,000,000,000 in the region.\n**(10)**\nBy refusing to clarify that these restoration funds will not count towards gross foreign exchange reserves, the IMF has misled the CEMAC member states and directly put tens of billions of dollars of IOCs investment in the region at risk.\n#### 3. Statement of policy\nIt is the policy of the United States that\u2014\n**(1)**\nthe presence of United States companies is a good thing for the regions in which they invest;\n**(2)**\nany funds provided to the Bank of Central African States (in this Act referred to as BEAC ) by any extractive industry company for site rehabilitation are ineligible to count towards the gross foreign exchange reserves of a member state of the Central African Economic Monetary Community (in this Act referred to as CEMAC ) based on the requirements of the Balance of Payments and International Investment Position Manual of the International Monetary Fund (in this Act referred to as the IMF );\n**(3)**\nthe IMF has a responsibility to accurately clarify to countries what are eligible and ineligible assets to count towards the gross foreign exchange reserves of a country, so that countries are able to create appropriate financial policies; and\n**(4)**\nthe IMF would be responsible for the loss of investment that the CEMAC region would face if a foreign exchange regulation that mandates extractive industry companies repatriate restoration funds for site rehabilitation to the BEAC is enacted.\n#### 4. Withdrawal of funding\n##### (a) In general\nUntil the Secretary of the Treasury, in coordination with the United States Executive Director at the IMF and the Secretary of State, makes the determination described in subsection (b)\u2014\n**(1)**\nneither the President nor any person or agency shall, on behalf of the United States, vote to approve any action by the IMF relating to any CEMAC member state; and\n**(2)**\nthe Secretary of the Treasury shall direct the United States Executive Director at the IMF to use the voice and vote of the United States to oppose any proposal to\u2014\n**(A)**\nincrease the quota in the IMF for any CEMAC member state; or\n**(B)**\nmodify the exceptional access policy of the IMF for any CEMAC member state.\n##### (b) Determination\nThe determination referred to in subsection (a) is a determination that the IMF has publicly clarified that any funds provided to BEAC by any international oil company for site rehabilitation are ineligible to count towards the gross foreign exchange reserves of any country.\n##### (c) Publication\nOn making the determination described in subsection (b), the Secretary of the Treasury shall publicize the determination and transmit a copy of the determination to the appropriate congressional committees.\n##### (d) Report\nNo later than 30 days after the date the determination described in subsection (b) is made, and no later than 180 days after the enactment of this Act if the determination has, by then, not been made, the Secretary of the Treasury shall provide to the appropriate congressional committees a report that details the actions taken by the United States Government at the International Monetary Fund, including those by the United States Executive Director at the IMF, to have the IMF publicly clarify that any funds provided to BEAC by any international oil company for site rehabilitation are ineligible to count towards the gross foreign exchange reserves of a country.\n##### (e) Appropriate congressional committees\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Financial Services and the Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Finance and the Committee on Foreign Relations of the Senate.",
      "versionDate": "2025-03-25",
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
        "name": "International Affairs",
        "updateDate": "2025-05-14T12:57:51Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2325ih.xml"
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
      "title": "CEMAC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CEMAC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Central African Exploitation and Manipulation of American Companies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To withhold United States support for any action in the International Monetary Fund relating to member states of the Central African Economic Monetary Community until a determination as to gross foreign exchange reserves is made.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:45Z"
    }
  ]
}
```
