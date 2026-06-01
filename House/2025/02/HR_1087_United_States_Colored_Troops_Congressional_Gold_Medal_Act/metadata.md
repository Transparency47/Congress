# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1087?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1087
- Title: United States Colored Troops Congressional Gold Medal Act
- Congress: 119
- Bill type: HR
- Bill number: 1087
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:21:17Z
- Update date including text: 2025-12-05T21:21:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR E104-105)
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR E104-105)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1087",
    "number": "1087",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "United States Colored Troops Congressional Gold Medal Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:21:17Z",
    "updateDateIncludingText": "2025-12-05T21:21:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E104-105)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:00:20Z",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "RI"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CT"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1087ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1087\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Norton (for herself, Mr. Amo , Mr. Beyer , Mr. Carter of Louisiana , Mr. Grijalva , Mrs. Hayes , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo posthumously award a Congressional Gold Medal, collectively, to the African Americans who served with Union forces during the Civil War, in recognition of their bravery and outstanding service.\n#### 1. Short title\nThis Act may be cited as the United States Colored Troops Congressional Gold Medal Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSince the colonial era, African Americans have served the United States in times of war.\n**(2)**\nDuring the Civil War, approximately 200,000 African-American men served in the Union Army and 19,000 African-American men served in the Union Navy.\n**(3)**\nDuring the Civil War, African-American women were not allowed to formally enlist as soldiers or sailors, though they served as nurses, cooks, spies, and scouts for the Union Army and the Union Navy.\n**(4)**\nWhile African-American men served in the Navy since its establishment, there was resistance to enlisting them to take up arms for the Union Army at the start of the Civil War.\n**(5)**\nAs the Civil War dragged on, President Lincoln broke from the previous policy of his administration and determined that liberating enslaved persons was a military necessity absolutely essential for the salvation of the Union .\n**(6)**\nThe Act entitled An Act to suppress insurrection, to punish treason and rebellion, to seize and confiscate the property of rebels, and for other purposes , approved July 17, 1862 (commonly known as the Second Confiscation Act ) (12 Stat. 589; chapter 195), and the Act of July 17, 1862 (commonly known as the Military Act of 1862 ) (12 Stat. 597; chapter 201), were the first official authorizations to employ African Americans in the Union Army.\n**(7)**\nIt was not until January 1, 1863, the effective date of the Emancipation Proclamation issued by President Lincoln, that the Union Army was ordered to receive African-American men.\n**(8)**\nOn May 22, 1863, the United States War Department issued General Order Number 143, which established the Bureau of Colored Troops for the recruitment and organization of regiments of the Union Army composed of African-American men, called the United States Colored Troops (referred to in this section as USCT ).\n**(9)**\nLeaders such as Frederick Douglass encouraged African Americans to enlist to advance the cause of citizenship. Once let the black man get upon his person the brass letters, U.S. , let him get an eagle on his button, and a musket on his shoulder and bullets in his pocket, there is no power on [E]arth that can deny that he has earned the right to citizenship. , wrote Douglass.\n**(10)**\nAfrican-American sailors constituted a significant segment of the Union Navy, making up 20 percent of the total enlisted force of the Navy.\n**(11)**\nAlthough there were rank restrictions on African Americans in the Navy before the Civil War, this policy changed after the establishment of the USCT, when the Union Navy started to compete with the Union Army for enlistment of African Americans.\n**(12)**\nYet, in practice, most African Americans could not advance beyond lowest ranks of boy and landsman.\n**(13)**\nAfrican-American soldiers and sailors served with distinction, honor, and bravery amid racial discrimination and adverse circumstances, including the risk of enslavement and torture if captured.\n**(14)**\nEighteen members of the USCT and 8 African-American sailors were awarded the Medal of Honor, the highest honor in the United States for bravery in combat.\n**(15)**\nFor generations after the Civil War, the contributions of African Americans in the Civil War were excluded from historical memory.\n**(16)**\nPublic Law No. 102\u2013412 (106 Stat. 2104) authorized the establishment of a memorial on Federal land in the District of Columbia to honor African Americans who served with Union forces during the Civil War.\n**(17)**\nThis memorial, featuring a bronze statue of USCT soldiers, an African-American sailor and family, is surrounded by the Wall of Honor, which lists the names of the members of the USCT.\n**(18)**\nThe African American Civil War Museum is located in the District of Columbia.\n**(19)**\nPatriots and heroes who rose in service to a Nation that would not fully recognize them, the African Americans who served the Union during the Civil War deserve our recognition for their contributions to the grant of emancipation and citizenship for nearly 4,000,000 enslaved people and the preservation of the Union.\n#### 3. Congressional Gold Medal\n##### (a) Presentation authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the posthumous presentation, on behalf of Congress, of a gold medal of appropriate design to the African Americans who served with Union forces during the Civil War, collectively, in recognition of their bravery and outstanding service during the Civil War.\n##### (b) Design and striking\nFor the purposes of the award referred to in subsection (a), the Secretary of the Treasury (hereafter in this Act referred to as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian Institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the Smithsonian Institution, where the medal shall be available for display as appropriate and available for research.\n**(2) Sense of the Congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal received under paragraph (1) available for display elsewhere, particularly at appropriate locations associated with the United States Colored Troops.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck pursuant to section 3 at a price sufficient to cover the cost thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nThe medals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of section 5134 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the cost of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals under section 4 shall be deposited in the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-10",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "498",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United States Colored Troops Congressional Gold Medal Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "Smithsonian Institution",
            "updateDate": "2025-06-09T17:43:16Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-06-09T17:43:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-05T13:33:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1087",
          "measure-number": "1087",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1087v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Colored Troops Congressional Gold Medal Act</strong></p> <p>This bill provides for the award of a Congressional Gold Medal posthumously to the African Americans who served with Union forces in recognition of their bravery and outstanding service during the Civil War.</p>"
        },
        "title": "United States Colored Troops Congressional Gold Medal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1087.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Colored Troops Congressional Gold Medal Act</strong></p> <p>This bill provides for the award of a Congressional Gold Medal posthumously to the African Americans who served with Union forces in recognition of their bravery and outstanding service during the Civil War.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1087"
    },
    "title": "United States Colored Troops Congressional Gold Medal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Colored Troops Congressional Gold Medal Act</strong></p> <p>This bill provides for the award of a Congressional Gold Medal posthumously to the African Americans who served with Union forces in recognition of their bravery and outstanding service during the Civil War.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1087"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1087ih.xml"
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
      "title": "United States Colored Troops Congressional Gold Medal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Colored Troops Congressional Gold Medal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To posthumously award a Congressional Gold Medal, collectively, to the African Americans who served with Union forces during the Civil War, in recognition of their bravery and outstanding service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:45Z"
    }
  ]
}
```
