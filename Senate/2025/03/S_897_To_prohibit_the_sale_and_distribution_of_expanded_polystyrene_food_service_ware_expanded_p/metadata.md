# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/897?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/897
- Title: Farewell to Foam Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 897
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-05T22:04:11Z
- Update date including text: 2025-12-05T22:04:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/897",
    "number": "897",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Farewell to Foam Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:04:11Z",
    "updateDateIncludingText": "2025-12-05T22:04:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T20:26:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-06",
      "state": "ME"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-06",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s897is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 897\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Van Hollen (for himself, Mr. Blumenthal , Mr. Booker , Mr. Durbin , Mr. King , Mr. Markey , Mr. Merkley , Mr. Padilla , Mr. Sanders , Ms. Warren , Mr. Welch , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the sale and distribution of expanded polystyrene food service ware, expanded polystyrene loose fill, and expanded polystyrene coolers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farewell to Foam Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Biological product**\nThe term biological product has the meaning given the term in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ).\n**(3) Covered polystyrene foam ware**\nThe term covered polystyrene foam ware means\u2014\n**(A)**\nan expanded polystyrene cooler;\n**(B)**\nan expanded polystyrene food service ware; and\n**(C)**\nexpanded polystyrene loose fill.\n**(4) Distributor**\nThe term distributor means any person that distributes covered polystyrene foam ware that is sold or offered for sale in the United States.\n**(5) Drug**\nThe term drug has the meaning given the term in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(6) Expanded polystyrene**\nThe term expanded polystyrene means blown polystyrene and expanded or extruded foams that are thermoplastic petrochemical materials utilizing a styrene monomer and processed by any technique or combination of techniques, including fusion of polymer spheres (expandable bead polystyrene), injection molding, foam molding, and extrusion-blow molding (extruded foam polystyrene).\n**(7) Expanded polystyrene cooler**\n**(A) In general**\nThe term expanded polystyrene cooler means a portable container made entirely or partially of expanded polystyrene that is designed or intended to be used for cold storage.\n**(B) Exclusion**\nThe term expanded polystyrene cooler excludes portable containers intended to be used for drugs, medical devices, or biological products.\n**(8) Expanded polystyrene food service ware**\n**(A) In general**\nThe term expanded polystyrene food service ware means a product made of expanded polystyrene that is\u2014\n**(i)**\nused for selling or providing food or beverages; and\n**(ii)**\n**(I)**\nintended by the manufacturer to be used once for eating or drinking; or\n**(II)**\ngenerally recognized by the public as an item to be discarded after 1 use.\n**(B) Inclusions**\nThe term expanded polystyrene food service ware includes any product described in subparagraph (A) consisting of a bowl, plate, hot or cold beverage cup, lid, clamshell, tray, carton for eggs or other food, or any other item used for serving or containing prepared food, including takeout food and leftovers from partially consumed meals prepared by food vendors.\n**(9) Expanded polystyrene loose fill**\nThe term expanded polystyrene loose fill means a void-filling packaging product made of expanded polystyrene foam that is used as a packaging fill (commonly referred to as packing peanuts ).\n**(10) Food service provider**\nThe term food service provider means a person engaged in the business of selling or distributing prepared food or beverages for on-premise or off-premise consumption, including any\u2014\n**(A)**\nfood service establishment, caterer, temporary food service establishment, mobile food service establishment, and pushcart;\n**(B)**\nretail food store;\n**(C)**\ndelicatessen;\n**(D)**\ngrocery store;\n**(E)**\nrestaurant;\n**(F)**\ncafeteria;\n**(G)**\ncoffee shop;\n**(H)**\nhospital, adult care facility, and nursing home; and\n**(I)**\nelementary or secondary school, college, and university.\n**(11) Manufacturer**\nThe term manufacturer means any person that manufactures or imports covered polystyrene foam ware that is sold, offered for sale, or distributed in the United States.\n**(12) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(13) Prepared food**\n**(A) In general**\nThe term prepared food means food or beverages that\u2014\n**(i)**\nare cooked, chopped, sliced, mixed, brewed, frozen, heated, squeezed, combined, or otherwise prepared on the premises of a food service provider for immediate consumption; and\n**(ii)**\nrequire no further preparation to be consumed.\n**(B) Inclusion**\nThe term prepared food includes ready-to-eat takeout foods and beverages described in subparagraph (A).\n**(14) Retailer**\nThe term retailer means any person that sells, supplies, or offers to consumers covered polystyrene foam ware.\n#### 3. Ban on expanded polystyrene food service ware, loose fill, and coolers\n##### (a) Expanded polystyrene food service ware\nBeginning on January 1, 2028, no food service provider, manufacturer, distributor, or retailer shall sell, offer for sale, or distribute expanded polystyrene food service ware.\n##### (b) Expanded polystyrene loose fill and expanded polystyrene coolers\nBeginning on January 1, 2028, no manufacturer, distributor, or retailer shall sell, offer for sale, or distribute expanded polystyrene loose fill or expanded polystyrene coolers.\n#### 4. Enforcement\n##### (a) Written notification for first violation\nIf a food service provider, manufacturer, distributor, or retailer violates section 3, the Administrator shall provide that food service provider, manufacturer, distributor, or retailer with written notification regarding the violation.\n##### (b) Subsequent violations\n**(1) In general**\nIf a food service provider, manufacturer, distributor, or retailer, subsequent to receiving a written notification under subsection (a), violates section 3 again, the Administrator shall impose a civil penalty on the food service provider, manufacturer, distributor, or retailer in accordance with this subsection.\n**(2) Amount of penalty**\nFor each violation described in paragraph (1), the amount of the civil penalty under that paragraph shall be\u2014\n**(A)**\nin the case of the second violation, $250;\n**(B)**\nin the case of the third violation, $500; and\n**(C)**\nin the case of the fourth, and any subsequent, violation, $1,000.\n**(3) Limitations**\n**(A) Food service providers; retailers**\nIn the case of a food service provider or retailer the annual revenue of which is less than $1,000,000, a penalty shall not be imposed under this subsection more than once during any 7-day period.\n**(B) Manufacturer; distributors**\nIn the case of a manufacturer or distributor the annual revenue of which is less than $5,000,000, a penalty shall not be imposed under this subsection more than once during any 7-day period.\n##### (c) State enforcement\nThe Administrator may permit a State to carry out enforcement under this section if the Administrator determines that the State meets such requirements as the Administrator may establish.\n#### 5. Regulations\nThe Administrator may promulgate such regulations as the Administrator determines necessary to carry out this Act.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1918",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farewell to Foam Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-28T12:16:41Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s897is.xml"
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
      "title": "Farewell to Foam Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farewell to Foam Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the sale and distribution of expanded polystyrene food service ware, expanded polystyrene loose fill, and expanded polystyrene coolers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:29Z"
    }
  ]
}
```
