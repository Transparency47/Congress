# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2593?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2593
- Title: PROTECT the Grid Act
- Congress: 119
- Bill type: S
- Bill number: 2593
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-02-18T16:07:13Z
- Update date including text: 2026-02-18T16:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2593",
    "number": "2593",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PROTECT the Grid Act",
    "type": "S",
    "updateDate": "2026-02-18T16:07:13Z",
    "updateDateIncludingText": "2026-02-18T16:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
        "item": {
          "date": "2025-07-31T18:15:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2593is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2593\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Secretary of Commerce to submit a report assessing vulnerabilities to the electric grid in the United States from certain Internet-connected devices and applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Remote Operations by Threatening Entities on Critical Technology for the Grid Act or the PROTECT the Grid Act .\n#### 2. Findings; Purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe rapid proliferation of high\u2011wattage IoT devices, such as electric vehicle chargers, clothes dryers, smart air conditioners, water heaters, ovens, and similar appliances, has dramatically increased the number of connected devices in households in the United States;\n**(2)**\n**(A)**\nsmart appliance applications and software platforms increasingly serve as remote control interfaces; and\n**(B)**\nwhen those applications and software platforms originate from companies operating under the jurisdiction or direction of foreign adversaries they offer a pathway for large-scale, coordinated manipulation of power demand, threatening grid stability;\n**(3)**\n**(A)**\nin certain foreign adversary jurisdictions, particularly the People\u2019s Republic of China, private companies are subject to formal political oversight through mechanisms such as, in the case of the People\u2019s Republic of China, embedded Chinese Communist Party committees and executive-level Chinese Communist Party leadership; and\n**(B)**\nthose arrangements blur the lines between commercial activity and state-directed strategic interests;\n**(4)**\nfurther elevating the risk to the United States electric grid is the 2017 Cybersecurity Law of the People\u2019s Republic of China (commonly referred to as the Chinese Cybersecurity Law ), which mandates that Chinese companies store customer data domestically and grant Chinese state authorities broad access to those data;\n**(5)**\nthe legal and political structures described in paragraphs (3) and (4) increase the likelihood that connected home appliances could be leveraged by foreign adversaries to target critical infrastructure in the event of a conflict with the United States;\n**(6)**\ncompanies controlled by foreign adversaries\u2014\n**(A)**\nare actively pursuing rapid deployment of high-wattage IoT devices that could be used to attack the electric grid in the United States; and\n**(B)**\ncontrol more than 25 percent of the major appliance industry in the United States, which provides an established platform for quickly deploying those high-wattage IoT devices;\n**(7)**\nthrough smart applications, companies controlled by foreign adversaries\u2014\n**(A)**\nare actively collecting detailed consumer data on millions of people in the United States; and\n**(B)**\nhave the ability to directly manipulate the demand of high-wattage devices on the electric grid;\n**(8)**\nas a result, foreign adversary-controlled applications for high\u2011wattage IoT devices create significant risk of coordinated, deliberate, demand-manipulation attacks on the electric grid in the United States;\n**(9)**\nseveral academic studies from researchers at Princeton University, the Georgia Institute of Technology, and the University of California, Santa Cruz, point to significant risks of manipulation of demand via IoT (commonly referred to as MaDIoT ) attacks to manipulate power demand on the electric grid that could result in large-scale blackouts and potential damage to the electric grid;\n**(10)**\nit is therefore critical to protect energy infrastructure in the United States by ensuring that smart applications embedded in home appliances are secure and cannot serve as an entry point for foreign adversaries; and\n**(11)**\nfailing to address the vulnerabilities presented by those smart applications could lead to grid instability, frequency imbalances, cascading system failures, and, ultimately, catastrophic disruptions that jeopardize both public safety and the broader economy of the United States.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto harmonize and reinforce existing national security initiatives aimed at securing the domestic information and communications technology and services (commonly referred to as ICTS ) supply chain against manipulation of demand, especially by the People\u2019s Republic of China; and\n**(2)**\nto direct the Secretary of Commerce, in consultation with other relevant Federal officials, to submit to Congress a report containing findings and recommendations to ensure that network-connected home appliances in households in the United States do not serve as a conduit for activities by foreign adversaries or jeopardize the stability of the electric grid in the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Consumer product**\nThe term consumer product has the meaning given the term in section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ).\n**(2) Covered entity**\nThe term covered entity means an entity that\u2014\n**(A)**\nis subject to the jurisdiction of a foreign adversary;\n**(B)**\nis directly or indirectly operating on behalf of a foreign adversary; or\n**(C)**\nis owned by, directly or indirectly controlled by, or otherwise subject to the direction or influence of, a foreign adversary.\n**(3) Critical infrastructure**\nThe term critical infrastructure has the meaning given the term in subsection (e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c ).\n**(4) Foreign adversary**\nThe term foreign adversary means\u2014\n**(A)**\nany covered nation (as defined in section 4872(f) of title 10, United States Code); and\n**(B)**\nthe Bolivarian Republic of Venezuela while Nicol\u00e1s Maduro Moros is in power.\n**(5) Foreign adversary-controlled application**\nThe term foreign adversary-controlled application means a website, desktop application, mobile application, or augmented or immersive technology application that is operated, directly or indirectly (including through a parent, subsidiary, or affiliate (as those terms are defined in section 230.405 of title 17, Code of Federal Regulations (as in effect on the date of enactment of this Act))), by a covered entity.\n**(6) High-wattage IoT device**\nThe term high-wattage IoT device means any Internet\u2011connected appliance or device that is capable of consuming or controlling electrical power at a level exceeding 500 watts, regardless of whether the device is used or designed for use in residential or commercial applications.\n**(7) IoT**\nThe term IoT means Internet of Things.\n**(8) Relevant Federal official**\nThe term relevant Federal official means\u2014\n**(A)**\nany Federal official described in section 1(a) of Executive Order 13873 (84 Fed. Reg. 22689; relating to securing the information and communications technology and services supply chain) (as in effect on the date of enactment of this Act) (or a designee of the applicable Federal official); and\n**(B)**\nthe head (or a designee of the head) of any other Federal department or agency that, in the determination of the Secretary of Commerce, is relevant to the purposes of this Act.\n#### 4. Report on national security risks posed by foreign adversary-controlled applications with the capability of controlling high-wattage IoT devices\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Secretary of Commerce, in coordination with other relevant Federal officials, shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report assessing the national security risks associated with foreign adversary-controlled applications with the ability to attack or undermine critical infrastructure in the United States.\n##### (b) Considerations\nIn preparing the report under subsection (a), the Secretary of Commerce shall consider, at a minimum\u2014\n**(1)**\nthe extent of deployment of high-wattage IoT devices across the United States;\n**(2)**\nrisks relating to foreign adversary-controlled applications, especially those incorporated into consumer products that could be used to attack or otherwise destabilize the electric grid;\n**(3)**\npotential impacts of those risks and any other relevant vulnerabilities on national security, including the risks of frequency imbalances, cascading failures, and other disruptions to critical infrastructure; and\n**(4)**\npublic comments and input from industry experts, domestic producers, importers, consumer groups, and other stakeholders regarding the security of, and the extent of foreign influence over, foreign adversary-controlled applications and high-wattage IoT devices.\n##### (c) Recommendations\nThe report submitted under subsection (a) shall include recommendations for mitigation measures to address any identified national security risks, which may include\u2014\n**(1)**\nan assessment of how Executive Order 13873 (84 Fed. Reg. 22689; relating to securing the information and communications technology and services supply chain) (as in effect on the date of enactment of this Act) may be applied to IoT devices, as such devices apply to the electric grid, to include restrictions or conditions on transactions directly involving foreign adversary-controlled applications in high-wattage IoT devices;\n**(2)**\nspecifically restricting the procurement by the Federal Government of consumer products with a foreign adversary-controlled application;\n**(3)**\ncertification or labeling requirements for high-wattage IoT devices; and\n**(4)**\nany other proposal, as determined necessary by the Secretary of Commerce, in consultation with other relevant Federal officials.\n#### 5. Codification of Executive Order 13873\n##### (a) In general\nThe provisions of Executive Order 13873 (84 Fed. Reg. 22689; relating to securing the information and communications technology and services supply chain) (as in effect on the date of enactment of this Act) are enacted into law.\n##### (b) Publication\nIn publishing this Act in slip form and in the United States Statutes at Large pursuant to section 112 of title 1, United States Code, the Archivist of the United States shall include after the date of approval at the end an appendix setting forth the text of the Executive order referred to in subsection (a) (as in effect on the date of enactment of this Act).",
      "versionDate": "2025-07-31",
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
        "actionDate": "2026-01-22",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Foreign Affairs, Oversight and Government Reform, Ways and Means, Intelligence (Permanent Select), and Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7208",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT the Grid Act",
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
        "name": "Energy",
        "updateDate": "2025-09-18T18:15:46Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2593is.xml"
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
      "title": "PROTECT the Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT the Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Remote Operations by Threatening Entities on Critical Technology for the Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Commerce to submit a report assessing vulnerabilities to the electric grid in the United States from certain Internet-connected devices and applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:59Z"
    }
  ]
}
```
