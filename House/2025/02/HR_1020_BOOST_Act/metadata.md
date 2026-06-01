# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1020?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1020
- Title: BOOST Act
- Congress: 119
- Bill type: HR
- Bill number: 1020
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-05-22T15:27:33Z
- Update date including text: 2025-05-22T15:27:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1020",
    "number": "1020",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "BOOST Act",
    "type": "HR",
    "updateDate": "2025-05-22T15:27:33Z",
    "updateDateIncludingText": "2025-05-22T15:27:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:00:30Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CO"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1020ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1020\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Moolenaar (for himself, Mr. Bishop , Mr. Huizenga , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a refundable credit against tax for the purchase of communications signal boosters in areas with inadequate broadband internet access service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Broadening Online Opportunities through Simple Technologies Act or the BOOST Act .\n#### 2. Broadband Internet communications signal booster credit\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 37 the following new section:\n36C. Broadband Internet communications signal booster credit (a) In general In the case of an individual who elects the application of this section, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to 75 percent of so much of the qualified signal booster expenditures of the taxpayer for the taxable year as does not exceed $400. (b) Qualified signal booster expenditures For purposes of this section\u2014 (1) In general The term qualified signal booster expenditures means amounts paid or incurred by the taxpayer for the purchase of\u2014 (A) any communications signal booster, (B) any customer premises equipment for use with satellite networks, and (C) any ground station equipment to send and receive transmissions from satellite networks, for use by the taxpayer in a principal residence (within the meaning of section 121) of the taxpayer which is located in an unserved area. (2) Communications signal booster The term communications signal booster means a device the first use of which is with the taxpayer and that receives a wireless signal, or a commercial mobile data service (as defined in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 )) signal\u2014 (A) in order to increase the strength or range of such signal, and (B) in connection with retransmitting a broadband internet access service signal. (3) Unserved area The term unserved area means an area eligible for funding under phase 1 or phase 2 of the Rural Digital Opportunity Fund established by the Federal Communications Commission in the Report and Order in the matter of Rural Digital Opportunity Fund and Connect America Fund that was adopted by the Commission on January 30, 2020 (FCC 20\u20135). (4) Broadband internet access service The term broadband internet access service has the meaning given such term in section 8.1(b) of title 47, Code of Federal Regulations (or any successor regulation). (c) Credit allowed for only 1 taxable year An election by the taxpayer to have this section apply may not be made for any taxable year if such an election is in effect for the taxpayer for any preceding taxable year. (d) Regulations and guidance The Secretary shall, in consultation with the Federal Communications Commission, prescribe such regulations, and provide such other guidance, as may be necessary to carry out the purposes of this section including a program for persons engaged in the trade or business of selling communications signal boosters, or any other equipment described in subsection (b)(1), to voluntarily report any such sale in an unserved area. (e) Termination This section shall not apply to any amounts paid or incurred in any taxable year beginning after December 31, 2029. .\n##### (b) Clerical amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of such Code is amended by inserting before the item relating to section 26 the following new item:\nSec. 36C. Broadband Internet communications signal booster credit. .\n##### (c) Conforming amendment\nSection 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-05",
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
        "updateDate": "2025-04-01T14:42:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1020",
          "measure-number": "1020",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1020v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Broadening Online Opportunities through Simple Technologies Act or the BOOST Act</strong></p><p>This bill establishes a new refundable tax credit, through 2029, for expenses paid to purchase a Wi-Fi signal booster for use in a principal residence. (Some limitations apply.)</p><p>The bill allows a taxpayer located in an unserved area a one-time, refundable tax credit for 75% (up to $400) of expenses paid to purchase</p><ul><li>a communications signal booster (any device that receives a wireless signal or a commercial data service signal in order to increase the strength or range of the signal and in connection with\u00a0retransmitting a broadband internet access service signal),</li><li>any customer premises equipment for use with satellite networks, or</li><li>any ground station equipment to send and receive transmissions from satellite networks.</li></ul><p>Under the bill, an <em>unserved area</em> is defined as an area eligible for certain funding under the Rural Digital Opportunity Fund (generally areas where internet speeds are below 25 megabits per second for downloading and 3 megabits per second for uploading).</p><p>Finally, under the bill, the Department of the Treasury is required to issue regulations and\u00a0guidance on the new tax credit and a program for sellers of signal boosters to voluntarily report sales of such devices in\u00a0unserved areas.</p>"
        },
        "title": "BOOST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1020.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadening Online Opportunities through Simple Technologies Act or the BOOST Act</strong></p><p>This bill establishes a new refundable tax credit, through 2029, for expenses paid to purchase a Wi-Fi signal booster for use in a principal residence. (Some limitations apply.)</p><p>The bill allows a taxpayer located in an unserved area a one-time, refundable tax credit for 75% (up to $400) of expenses paid to purchase</p><ul><li>a communications signal booster (any device that receives a wireless signal or a commercial data service signal in order to increase the strength or range of the signal and in connection with\u00a0retransmitting a broadband internet access service signal),</li><li>any customer premises equipment for use with satellite networks, or</li><li>any ground station equipment to send and receive transmissions from satellite networks.</li></ul><p>Under the bill, an <em>unserved area</em> is defined as an area eligible for certain funding under the Rural Digital Opportunity Fund (generally areas where internet speeds are below 25 megabits per second for downloading and 3 megabits per second for uploading).</p><p>Finally, under the bill, the Department of the Treasury is required to issue regulations and\u00a0guidance on the new tax credit and a program for sellers of signal boosters to voluntarily report sales of such devices in\u00a0unserved areas.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr1020"
    },
    "title": "BOOST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadening Online Opportunities through Simple Technologies Act or the BOOST Act</strong></p><p>This bill establishes a new refundable tax credit, through 2029, for expenses paid to purchase a Wi-Fi signal booster for use in a principal residence. (Some limitations apply.)</p><p>The bill allows a taxpayer located in an unserved area a one-time, refundable tax credit for 75% (up to $400) of expenses paid to purchase</p><ul><li>a communications signal booster (any device that receives a wireless signal or a commercial data service signal in order to increase the strength or range of the signal and in connection with\u00a0retransmitting a broadband internet access service signal),</li><li>any customer premises equipment for use with satellite networks, or</li><li>any ground station equipment to send and receive transmissions from satellite networks.</li></ul><p>Under the bill, an <em>unserved area</em> is defined as an area eligible for certain funding under the Rural Digital Opportunity Fund (generally areas where internet speeds are below 25 megabits per second for downloading and 3 megabits per second for uploading).</p><p>Finally, under the bill, the Department of the Treasury is required to issue regulations and\u00a0guidance on the new tax credit and a program for sellers of signal boosters to voluntarily report sales of such devices in\u00a0unserved areas.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr1020"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1020ih.xml"
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
      "title": "BOOST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BOOST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadening Online Opportunities through Simple Technologies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a refundable credit against tax for the purchase of communications signal boosters in areas with inadequate broadband internet access service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T04:03:33Z"
    }
  ]
}
```
