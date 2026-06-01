# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1294
- Title: BEST Facilitation Act
- Congress: 119
- Bill type: HR
- Bill number: 1294
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-04T02:18:23Z
- Update date including text: 2026-03-04T02:18:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-13 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-13 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1294",
    "number": "1294",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "BEST Facilitation Act",
    "type": "HR",
    "updateDate": "2026-03-04T02:18:23Z",
    "updateDateIncludingText": "2026-03-04T02:18:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:10:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-13T18:18:20Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1294ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1294\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Ciscomani (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo pilot the use of image technician positions in the U.S. Customs and Border Protection Office of Field Operations.\n#### 1. Short titles\nThis Act may be cited as the Border Enforcement, Security, and Trade Facilitation Act of 2025 or the BEST Facilitation Act .\n#### 2. Office of Field Operations image technician pilot program\n##### (a) In general\nSection 411(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 211(g) ) is amended by adding at the end the following:\n(6) Image technician pilot program (A) Image technician 1 (i) In general There shall be in the Office of Field Operations, Image Technician 1 positions, which shall be filled in accordance with the provisions under chapter 33 (relating to appointments in the competitive service) and chapters 51 and 53 (relating to classification and rates of pay) of title 5, United States Code. (ii) Conditions Image Technician 1 positions\u2014 (I) may be filled by existing U.S. Customs and Border Protection employees; (II) are not law enforcement officer positions; (III) may not be filled by independent contractors; and (IV) shall be assigned to a regional command center established under subparagraph (F). (iii) Duties The duties of an Image Technician 1 shall include\u2014 (I) reviewing non-intrusive inspection images of conveyances and containers entering or exiting the United States through a land, sea, or air port of entry or international rail crossing; (II) assessing whether images of conveyances and containers appear to contain anomalies indicating the potential presence of contraband, persons unlawfully seeking to enter or exit the United States, or illicitly concealed merchandise, including illicit drugs and terrorist weapons; (III) recommending entry release or exit release for any conveyances and containers whenever the images of such items do not include noticeable anomalies indicating the potential presence of contraband, persons seeking to unlawfully enter or exit the United States, or illicitly concealed merchandise, including illicit drugs or terrorist weapons, to the U.S. Customs and Border Protection Officer responsible for inspecting such conveyance or container; and (IV) recommending further inspection of any conveyances and containers whenever the Image Technician reasonably believes that an image of any such item contains anomalies indicating the potential presence of contraband, persons seeking to unlawfully enter or exit the United States, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons, to the U.S. Customs and Border Protection officer who is responsible for inspecting such conveyance or container. (B) Image technician 2 (i) In general There shall be in the Office of Field Operations, Image Technician 2 positions, which shall be filled in accordance with the provisions under chapter 33 (relating to appointments in the competitive service) and chapters 51 and 53 (relating to classification and rates of pay) of title 5, United States Code. (ii) Conditions Image Technician 2 positions\u2014 (I) may be filled by existing U.S. Customs and Border Protection employees; (II) are not law enforcement officer positions; (III) may not be filled by independent contractors; and (IV) shall be assigned to a regional command center established under subparagraph (F). (iii) Duties The duties of an Image Technician 2 shall include\u2014 (I) carrying out all of the duties described in subclauses (I) through (IV) of subparagraph (A)(ii); (II) receiving intelligence from the National Targeting Center regarding tactics, techniques, and procedures being used at ports of entry and in the border environment by malign actors to facilitate the unlawful entry or exit of contraband, persons, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons; and (III) reporting new information to the National Targeting Center regarding tactics, techniques, and procedures being used at ports of entry and in the border environment by malign actors to facilitate the unlawful entry or exit of contraband, persons, or concealed merchandise, such as illicit drugs or terrorist weapons. (C) Supervisory U.S. Customs and Border Protection Officers (i) Supervision All image technicians shall be supervised by a Supervisory U.S. Customs and Border Protection Officer. (ii) Discretion and decision-making authority The appropriate Supervisory U.S. Customs and Border Protection Officer, while working with image technicians, shall retain the discretion and final decision-making authority\u2014 (I) to release conveyances or cargo for entry; or (II) to refer such conveyance or cargo for further inspection. (iii) Training A Supervisory U.S. Customs and Border Protection Officer who supervises image technicians shall receive additional training in accordance with subparagraph (D). (D) Training requirements All image technicians shall receive annual training and additional ad hoc training, to the extent necessary based on current trends, regarding\u2014 (i) respecting privacy, civil rights, and civil liberties, including the protections against unreasonable searches and seizures afforded by the First and Fourth Amendments to the Constitution of the United States, as applicable and as interpreted by the Federal courts; (ii) analyzing images generated by non-intrusive inspection technologies or any successor technologies deployed by U.S. Customs and Border Protection; (iii) identifying commodities and merchandise in images generated by non-intrusive inspection technologies or any successor technologies deployed by U.S. Customs and Border Protection; (iv) identifying contraband, persons who are seeking to unlawfully enter or exit the United States, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons, in images generated by non-intrusive technologies or any successor technologies deployed by U.S. Customs and Border Protection; (v) tactics, techniques, and procedures being used at ports of entry and in the border environment by malign actors to facilitate the unlawful entry or exit of contraband, persons, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons; and (vi) any other training that the Commissioner of U.S. Customs and Border Protection determines to be relevant to the duties described in subparagraphs (A)(iii) or (B)(iii). (E) Annual assessment All image technicians shall receive annual testing with respect to their\u2014 (i) accuracy in image analysis; (ii) timeliness in image analysis; and (iii) ability to ascertain tactics, techniques, and procedures being used at ports of entry and in the border environment by malign actors to facilitate the unlawful entry or exit of contraband, persons, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons. (F) Command centers As part of the pilot program established under this paragraph, the Executive Assistant Commissioner of the Office of Field Operations shall establish 5 regional command centers at land, rail, air, and sea ports in which image technicians shall review non-intrusive inspection images. (G) Rule of construction Nothing in this paragraph may be construed to affect the discretion and final decision-making authority given to U.S. Customs and Border Protection Officers to release conveyances or cargo for entry or exit or to refer such conveyances or cargo for further inspection. .\n##### (b) Effective date\n**(1) Sunset**\nThe amendment made by subsection (a) shall cease to have effect on the date that is 5 years after the date of the enactment of this Act.\n**(2) Transfers authorized**\nUpon the termination of the pilot program established by section 411(g)(6) of the Homeland Security Act of 2002, as added by subsection (a), individuals occupying Image Technician 1 or Image Technician 2 positions in the Office of Field Operations may transfer to comparable positions within U.S. Customs and Border Protection or the Department of Homeland Security.\n#### 3. Reporting requirements\n##### (a) Semiannual reports\nNot later than 180 days after the hiring of the first positions described in section 411(g)(6) of the Homeland Security Act of 2002, as added by section 2, and every 180 days thereafter, the Commissioner of U.S. Customs and Border Protection, in consultation with the Executive Assistant Commissioner of the Office of Field Operations, shall submit a report to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives that identifies\u2014\n**(1)**\nthe number of Image Technician 1 and Image Technician 2 positions filled during the reporting period;\n**(2)**\nthe number of Image Technician 1 and Image Technician 2 positions currently employed by the Office of Field Operations, disaggregated by\u2014\n**(A)**\nport of entry or field office;\n**(B)**\nimage technician position; and\n**(C)**\ncommand center, as applicable;\n**(3)**\nthe daily average number of images scanned by each Image Technician 1 and each Image Technician 2;\n**(4)**\ntraining methodologies utilized to train image technicians;\n**(5)**\nassessment passage rates of image technicians;\n**(6)**\nthe impact of image technicians on interdiction rates at ports of entry and international rail crossings at which image technicians are stationed or from which image technicians review images, including\u2014\n**(A)**\nthroughput increases or decreases at such ports of entry and international rail crossings;\n**(B)**\nincreases or decreases in waiting times at such ports of entry and international rail crossings;\n**(C)**\naverage wait times at such ports of entry and international rail crossings; and\n**(D)**\nincreases or decreases of seizures of contraband, persons seeking to unlawfully enter or exit the United States, or illicitly concealed merchandise, such as illicit drugs or terrorist weapons, broken down by type of seizure and port of entry or international rail crossing;\n**(7)**\nthe impact of image technicians on U.S. Customs and Border Protection\u2019s capability to review non-intrusive inspection images of conveyances and containers entering or exiting the United States through a land, sea, or air port of entry or international rail crossing;\n**(8)**\nan assessment of the effectiveness with which image technicians carry out the duties described in subparagraphs (A)(iii) and (B)(iii) of section 411(g)(6) of the Homeland Security Act of 2002, as added by section 2(a), compared to any U.S. Customs and Border Protection officers who are assigned such duties.\n**(9)**\nthe progress made in establishing command centers under the pilot program established by such section;\n**(10)**\nany infrastructure or resource needs required to establish such command centers; and\n**(11)**\nthe ports of entry and international rail crossing, as applicable, that are supported by such a command center.\n##### (b) Biannual briefings\nThe Executive Assistant Commissioner of the Office of Field Operations shall provide biannual briefings to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives regarding the information described in the latest report submitted pursuant to subsection (a).",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "578",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BEST Facilitation Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-13T13:53:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1294",
          "measure-number": "1294",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1294v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Border Enforcement, Security, and Trade Facilitation Act of 2025 or the BEST Facilitation\u00a0Act</strong></p><p>This bill establishes a pilot program for positions within U.S. Customs and Border Protection (CBP) to review inspection images of vehicles and cargo entering or exiting the United States.</p><p>Specifically, the bill establishes\u00a0the position of image technician 1 within the CBP Office of Field Operations. An image technician must (1) review nonintrusive inspection images of vehicles and cargo entering or exiting the United States; (2) assess whether such vehicles and cargo contain contraband, illicit drugs, weapons, or persons seeking to unlawfully enter the United States; and (3) refer suspicious vehicles and cargo for further inspection by a CBP officer.\u00a0These reviews must take place at one of five regional command centers established pursuant to this pilot program.</p><p>The bill also establishes the position of image technician 2 with additional responsibilities, including receiving and reporting intelligence to the National Targeting Center about techniques used by malign actors to transport contraband, illicit drugs, weapons, and persons seeking to unlawfully enter the United States.</p><p>Image technicians must be supervised by a supervisory CBP officer.</p><p>The bill establishes annual training requirements for both positions, including training on privacy and civil liberties and how to analyze inspection images.</p><p>This pilot program ends five years after the date of enactment of this bill. Individuals employed as image technicians at the end of the pilot program may transfer to comparable positions within CBP or the Department of Homeland Security.\u00a0</p>"
        },
        "title": "BEST Facilitation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1294.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Border Enforcement, Security, and Trade Facilitation Act of 2025 or the BEST Facilitation\u00a0Act</strong></p><p>This bill establishes a pilot program for positions within U.S. Customs and Border Protection (CBP) to review inspection images of vehicles and cargo entering or exiting the United States.</p><p>Specifically, the bill establishes\u00a0the position of image technician 1 within the CBP Office of Field Operations. An image technician must (1) review nonintrusive inspection images of vehicles and cargo entering or exiting the United States; (2) assess whether such vehicles and cargo contain contraband, illicit drugs, weapons, or persons seeking to unlawfully enter the United States; and (3) refer suspicious vehicles and cargo for further inspection by a CBP officer.\u00a0These reviews must take place at one of five regional command centers established pursuant to this pilot program.</p><p>The bill also establishes the position of image technician 2 with additional responsibilities, including receiving and reporting intelligence to the National Targeting Center about techniques used by malign actors to transport contraband, illicit drugs, weapons, and persons seeking to unlawfully enter the United States.</p><p>Image technicians must be supervised by a supervisory CBP officer.</p><p>The bill establishes annual training requirements for both positions, including training on privacy and civil liberties and how to analyze inspection images.</p><p>This pilot program ends five years after the date of enactment of this bill. Individuals employed as image technicians at the end of the pilot program may transfer to comparable positions within CBP or the Department of Homeland Security.\u00a0</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1294"
    },
    "title": "BEST Facilitation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Border Enforcement, Security, and Trade Facilitation Act of 2025 or the BEST Facilitation\u00a0Act</strong></p><p>This bill establishes a pilot program for positions within U.S. Customs and Border Protection (CBP) to review inspection images of vehicles and cargo entering or exiting the United States.</p><p>Specifically, the bill establishes\u00a0the position of image technician 1 within the CBP Office of Field Operations. An image technician must (1) review nonintrusive inspection images of vehicles and cargo entering or exiting the United States; (2) assess whether such vehicles and cargo contain contraband, illicit drugs, weapons, or persons seeking to unlawfully enter the United States; and (3) refer suspicious vehicles and cargo for further inspection by a CBP officer.\u00a0These reviews must take place at one of five regional command centers established pursuant to this pilot program.</p><p>The bill also establishes the position of image technician 2 with additional responsibilities, including receiving and reporting intelligence to the National Targeting Center about techniques used by malign actors to transport contraband, illicit drugs, weapons, and persons seeking to unlawfully enter the United States.</p><p>Image technicians must be supervised by a supervisory CBP officer.</p><p>The bill establishes annual training requirements for both positions, including training on privacy and civil liberties and how to analyze inspection images.</p><p>This pilot program ends five years after the date of enactment of this bill. Individuals employed as image technicians at the end of the pilot program may transfer to comparable positions within CBP or the Department of Homeland Security.\u00a0</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1294"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1294ih.xml"
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
      "title": "BEST Facilitation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T15:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BEST Facilitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T15:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Border Enforcement, Security, and Trade Facilitation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T15:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To pilot the use of image technician positions in the U.S. Customs and Border Protection Office of Field Operations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T15:03:28Z"
    }
  ]
}
```
