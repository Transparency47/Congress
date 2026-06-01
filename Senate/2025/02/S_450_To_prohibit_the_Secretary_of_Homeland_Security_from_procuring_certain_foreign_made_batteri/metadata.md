# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/450?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/450
- Title: Decoupling from Foreign Adversarial Battery Dependence Act
- Congress: 119
- Bill type: S
- Bill number: 450
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-06T06:40:15Z
- Update date including text: 2025-12-06T06:40:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/450",
    "number": "450",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
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
    "title": "Decoupling from Foreign Adversarial Battery Dependence Act",
    "type": "S",
    "updateDate": "2025-12-06T06:40:15Z",
    "updateDateIncludingText": "2025-12-06T06:40:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T17:50:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s450is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 450\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Scott of Florida (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the Secretary of Homeland Security from procuring certain foreign-made batteries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Decoupling from Foreign Adversarial Battery Dependence Act .\n#### 2. Prohibition on availability of funds for procurement of certain batteries\n##### (a) In general\nBeginning on October 1, 2027, none of the funds authorized to be appropriated or otherwise made available for the Department of Homeland Security may be obligated to procure a battery produced by an entity specified in subsection (b).\n##### (b) Entities specified\nThe entities specified in this subsection are the following:\n**(1)**\nContemporary Amperex Technology Company, Limited (also known as CATL ).\n**(2)**\nBYD Company, Limited.\n**(3)**\nEnvision Energy, Limited.\n**(4)**\nEVE Energy Company, Limited.\n**(5)**\nGotion High-tech Company, Limited.\n**(6)**\nHithium Energy Storage Technology company, Limited.\n**(7)**\nAny entity on any list required under clauses (i), (ii), (iv), or (v) of section 2(d)(2)(B) of the Act entitled An Act to ensure that goods made with forced labor in the Xinjiang Autonomous Region of the People\u2019s Republic of China do not enter the United States market, and for other purposes , approved December 23, 2021 ( Public Law 117\u201378 ; 22 U.S.C. 6901 note) (commonly referred to as the Uyghur Forced Labor Prevention Act ).\n**(8)**\nAny entity identified by the Secretary of Defense as a Chinese military company pursuant to section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 10 U.S.C. 113 note).\n**(9)**\nAny entity included in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, or any successor regulation.\n**(10)**\nAny subsidiary or successor to an entity specified in paragraphs (1) through (9).\n##### (c) Treatment of production\nFor purposes of this section, a battery shall be treated as produced by an entity specified in subsection (b) if such entity\u2014\n**(1)**\nassembles or manufactures the final product that uses such battery; or\n**(2)**\ncreates or otherwise provides a majority of the components used in such battery.\n##### (d) Waivers\n**(1) Relating to assessment**\nThe Secretary of Homeland Security may waive the limitation under subsection (a) if the Secretary assesses in the affirmative all of the following:\n**(A)**\nThe batteries to be procured do not pose a national security, data, or infrastructure risk to the United States.\n**(B)**\nThere is no available alternative to procure batteries that are\u2014\n**(i)**\nof similar or better cost and quality; and\n**(ii)**\nproduced by an entity not specified in subsection (b).\n**(2) Relating To research**\nThe Secretary of Homeland Security may waive the limitation under subsection (a) if the Secretary determines that the batteries to be procured are for the sole purpose of research, evaluation, training, testing, or analysis.\n**(3) Congressional notification**\nNot later than 15 days after granting a waiver under this subsection, the Secretary of Homeland Security shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives a notification relating thereto.\n##### (e) Report\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives a report on the anticipated impacts on mission and costs on the Department of Homeland Security associated with carrying out this section, including with respect to the following components of the Department:\n**(1)**\nU.S. Customs and Border Protection, including the U.S. Border Patrol.\n**(2)**\nU.S. Immigration and Customs Enforcement, including Homeland Security Investigations.\n**(3)**\nThe United States Secret Service.\n**(4)**\nThe Transportation Security Administration.\n**(5)**\nThe United States Coast Guard.\n**(6)**\nThe Federal Protective Service.\n**(7)**\nThe Federal Emergency Management Agency.\n**(8)**\nThe Federal Law Enforcement Training Centers.\n**(9)**\nThe Cybersecurity and Infrastructure Security Agency.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-03-11",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1166",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Decoupling from Foreign Adversarial Battery Dependence Act",
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
            "name": "Asia",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "Foreign and international corporations",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-06-13T18:44:03Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-06-13T18:44:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-13T19:20:32Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s450",
          "measure-number": "450",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s450v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Decoupling from Foreign Adversarial Battery Dependence Act</strong></p><p>This bill prohibits the Department of Homeland Security (DHS) from using appropriated funds to procure a battery produced by certain entities, particularly six specific companies owned and operated in China. This prohibition begins on October 1, 2027.</p><p>The bill allows DHS to waive the prohibition if DHS assesses in the affirmative that (1)\u00a0the batteries to be procured do not pose a risk to U.S. national security, data, or infrastructure; and (2)\u00a0there is no available alternative to procure batteries that are of similar or better cost and quality and that are produced by an entity not specified in this bill.</p><p>DHS may also waive the prohibition upon a determination that the batteries to be procured are for the sole purpose of research, evaluation, training, testing, or analysis.</p><p>The bill requires DHS to notify Congress within 15 days after granting a waiver under this bill.</p><p>The bill also requires DHS to report to Congress on the anticipated impacts associated with carrying out this bill, including with respect to specified agencies of DHS.</p>"
        },
        "title": "Decoupling from Foreign Adversarial Battery Dependence Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s450.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Decoupling from Foreign Adversarial Battery Dependence Act</strong></p><p>This bill prohibits the Department of Homeland Security (DHS) from using appropriated funds to procure a battery produced by certain entities, particularly six specific companies owned and operated in China. This prohibition begins on October 1, 2027.</p><p>The bill allows DHS to waive the prohibition if DHS assesses in the affirmative that (1)\u00a0the batteries to be procured do not pose a risk to U.S. national security, data, or infrastructure; and (2)\u00a0there is no available alternative to procure batteries that are of similar or better cost and quality and that are produced by an entity not specified in this bill.</p><p>DHS may also waive the prohibition upon a determination that the batteries to be procured are for the sole purpose of research, evaluation, training, testing, or analysis.</p><p>The bill requires DHS to notify Congress within 15 days after granting a waiver under this bill.</p><p>The bill also requires DHS to report to Congress on the anticipated impacts associated with carrying out this bill, including with respect to specified agencies of DHS.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s450"
    },
    "title": "Decoupling from Foreign Adversarial Battery Dependence Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Decoupling from Foreign Adversarial Battery Dependence Act</strong></p><p>This bill prohibits the Department of Homeland Security (DHS) from using appropriated funds to procure a battery produced by certain entities, particularly six specific companies owned and operated in China. This prohibition begins on October 1, 2027.</p><p>The bill allows DHS to waive the prohibition if DHS assesses in the affirmative that (1)\u00a0the batteries to be procured do not pose a risk to U.S. national security, data, or infrastructure; and (2)\u00a0there is no available alternative to procure batteries that are of similar or better cost and quality and that are produced by an entity not specified in this bill.</p><p>DHS may also waive the prohibition upon a determination that the batteries to be procured are for the sole purpose of research, evaluation, training, testing, or analysis.</p><p>The bill requires DHS to notify Congress within 15 days after granting a waiver under this bill.</p><p>The bill also requires DHS to report to Congress on the anticipated impacts associated with carrying out this bill, including with respect to specified agencies of DHS.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s450"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s450is.xml"
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
      "title": "Decoupling from Foreign Adversarial Battery Dependence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Decoupling from Foreign Adversarial Battery Dependence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of Homeland Security from procuring certain foreign-made batteries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:04Z"
    }
  ]
}
```
