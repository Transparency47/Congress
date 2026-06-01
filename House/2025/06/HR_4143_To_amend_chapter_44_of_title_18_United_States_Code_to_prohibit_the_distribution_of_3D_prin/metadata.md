# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4143
- Title: 3D Printed Gun Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4143
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-12-05T21:47:13Z
- Update date including text: 2025-12-05T21:47:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4143",
    "number": "4143",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "3D Printed Gun Safety Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:47:13Z",
    "updateDateIncludingText": "2025-12-05T21:47:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:03:35Z",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "IL"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4143ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4143\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Moskowitz (for himself, Ms. Wasserman Schultz , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 44 of title 18, United States Code, to prohibit the distribution of 3D printer plans for the printing of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 3D Printed Gun Safety Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThree dimensional, or 3D , printing involves the programming of a 3D printing machine with a computer file that provides the schematics for the item to be printed.\n**(2)**\nRecent technological developments have allowed for the 3D printing of firearms and firearm parts, including parts made out of plastic, by unlicensed individuals in possession of relatively inexpensive 3D printers.\n**(3)**\nBecause 3D printing allows individuals to make their own firearms out of plastic, they may be able to evade detection by metal detectors at security checkpoints, increasing the risk that a firearm will be used to perpetrate violence on an airplane or other area where people congregate.\n**(4)**\nThe availability of online schematics for the 3D printing of firearms and firearm parts increases the risk that dangerous people, including felons, domestic abusers, and other people prohibited from possessing firearms under Federal law, will obtain a firearm through 3D printing.\n**(5)**\nOn June 7, 2013, an assailant used a gun he had constructed by himself to kill his father, brother, and 3 other people at Santa Monica College in California. The person had failed a background check when he tried to purchase a gun from a licensed gun dealer. The gun he used was made from an unfinished AR\u201315-style receiver, similar to a receiver that can now be made with a 3D printer.\n**(6)**\nFirearms tracing is a powerful investigative tool. When law enforcement agencies recover firearms that have been used in crimes, the agencies work with the Bureau of Alcohol, Tobacco, Firearms and Explosives to trace these firearms to their first retail purchaser. The agencies can use that information to investigate and solve the crimes. In 2024, the Bureau of Alcohol, Tobacco, Firearms and Explosives processed more than 639,295 trace requests.\n**(7)**\nFirearms tracing depends on the ability to identify firearms based on their serial number. Traditionally, when a firearm is manufactured domestically or imported from abroad, it is engraved with a serial number and markings that identify the manufacturer or importer, make, model, and caliber, and are unique to the firearm. Firearms made by unlicensed individuals with 3D printers, however, do not contain genuine serial numbers.\n**(8)**\nCriminals seek firearms without serial numbers because they cannot be traced. In July 2018, the Los Angeles Police Department completed a 6-month-long investigation that resulted in the seizure of 45 firearms, some of which had been assembled without serial numbers in order to be untraceable. In 2023, the Metropolitan Police Department in the District of Columbia recovered 407 ghost guns. If the schematics for 3D printing firearms and firearm parts are available online, people intending to commit gun crimes may create similarly untraceable firearms in order to avoid accountability for these crimes.\n**(9)**\nInterstate gun trafficking, including the trafficking of untraceable firearms, interferes with lawful commerce in firearms and significantly contributes to gun crime. The Bureau of Alcohol, Tobacco, Firearms and Explosives discovered 46,037 guns from 2017 to 2021 that were trafficked interstate.\n**(10)**\nThe proliferation of 3D-printed firearms threatens to undermine the entire Federal firearms regulatory scheme and to endanger public safety and national security. By making illegal the distribution of certain computer code that can be used automatically to program 3D printers and create firearms\u2014the only means of combating this unique threat\u2014Congress seeks not to regulate the rights of computer programmers under the First Amendment to the Constitution of the United States, but rather to curb the pernicious effects of untraceable\u2014and potentially undetectable\u2014firearms.\n#### 3. Prohibition\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) Distribution of code for 3D printed firearms It shall be unlawful for any person to intentionally distribute, over the internet or by means of the World Wide Web, digital instructions in the form of Computer Aided Design files or other code that can automatically program a 3-dimensional printer or similar device to produce a firearm or complete a firearm from an unfinished frame or receiver. .",
      "versionDate": "2025-06-25",
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
        "actionDate": "2025-06-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2165",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "3D Printed Gun Safety Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-15T10:41:21Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4143ih.xml"
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
      "title": "3D Printed Gun Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T02:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "3D Printed Gun Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 44 of title 18, United States Code, to prohibit the distribution of 3D printer plans for the printing of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:26Z"
    }
  ]
}
```
