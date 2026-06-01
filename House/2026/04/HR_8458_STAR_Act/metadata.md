# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8458
- Title: STAR Act
- Congress: 119
- Bill type: HR
- Bill number: 8458
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-04-28T05:53:24Z
- Update date including text: 2026-04-28T05:53:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8458",
    "number": "8458",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001200",
        "district": "9",
        "firstName": "Darren",
        "fullName": "Rep. Soto, Darren [D-FL-9]",
        "lastName": "Soto",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "STAR Act",
    "type": "HR",
    "updateDate": "2026-04-28T05:53:24Z",
    "updateDateIncludingText": "2026-04-28T05:53:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8458ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8458\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Soto (for himself and Mr. Dunn of Florida ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend title 51, United States Code, to authorize certain actions to protect certain facilities and assets from unmanned aircraft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Theft and Aerospace Reconnaissance Act or the STAR Act .\n#### 2. Protection of certain facilities and assets from unmanned aircraft\n##### (a) Authority To protect certain NASA facilities and assets from unmanned aircraft\n**(1) In general**\nSubchapter II of chapter 201 of title 51, United States Code, is amended by adding at the end the following new section:\n20118. Authority to take actions to protect certain NASA facilities and assets from unmanned aircraft (a) Authority Notwithstanding any other provision of law, the Administrator may take, and may authorize officers and employees of the Administration to take, such actions as are described in subsection (b) that are necessary to mitigate the threat an unmanned aircraft system or unmanned aircraft poses to the safety or security of a covered facility. (b) Actions described The actions described in this subsection are the following: (1) Detect, identify, monitor, and track an unmanned aircraft system or unmanned aircraft, without prior consent. (2) Warn the operator of such unmanned aircraft system or unmanned aircraft, as the case may be. (3) Disrupt control of such unmanned aircraft system or unmanned aircraft, as the case may be, without prior consent, including by disabling such unmanned aircraft system or unmanned aircraft, as the case may be, by intercepting electronic communications or otherwise interfering with such communications. (4) Seize or exercise control of such unmanned aircraft system or unmanned aircraft, as the case may be. (5) Seize or otherwise confiscate such unmanned aircraft system or unmanned aircraft, as the case may be. (6) Use reasonable force to disable, damage, or destroy such unmanned aircraft system or unmanned aircraft, as the case may be. (c) Forfeiture Any unmanned aircraft system or unmanned aircraft described in subsection (a) and seized by the Administrator is subject to forfeiture to the United States. (d) Signage The Administrator shall display on each covered facility a sign that includes information relating to the following: (1) The actions that may be taken pursuant to subsection (a). (2) Forfeiture under subsection (c). (e) Policy development The Administrator, in coordination with relevant offices of the Administration and the Attorney General, the Secretary of Defense, the Secretary of Homeland Security, and the Administrator of the Federal Aviation Administration, shall develop uniform policy for the following: (1) The actions that may be taken pursuant to subsection (a). (2) The actions that may be taken pursuant to subsection (a) of section 50925. (f) Determination Each year, the Administrator shall consult with the local law enforcement agency for each covered facility to determine the most effective and least hazardous means to take actions pursuant to subsection (a). (g) Liability Neither the Administrator nor the officers and employees of the Administration are entitled to assert any form of absolute or qualified immunity as a defense to liability under this section, but if an unmanned aircraft system or unmanned aircraft poses a threat described in subsection (a) and an action is taken pursuant to such subsection to mitigate such threat, the operator of such unmanned aircraft system or unmanned aircraft, as the case may be, is liable for damages caused by such action. (h) Reports (1) Local law enforcement agencies Not later than 30 days after an instance in which an action described in paragraphs (3) through (6) of subsection (b) is taken pursuant to subsection (a), the Administrator shall submit to the local law enforcement agency for the jurisdiction in which such action was taken a report on such instance, in a form specified by such agency. (2) Specified entities Not later than one year after the date of the enactment of this section and annually thereafter, the Administrator shall submit to the specified entities a report that includes for the annual period covered by such report information relating to the following: (A) The actions, if any, described in paragraphs (3) through (6) of subsection (b) and taken pursuant to subsection (a), including an identification of each instance in which such an action was so taken and the means through which such action was so taken. (B) The actions, if any, described in paragraphs (3) through (6) of subsection (b) of section 50925 and taken pursuant to subsection (a) of such section, including an identification of each instance in which such an action was so taken and the means through which such action was so taken. (C) For each action referred to in subparagraph (A) or (B), the justification for so taking such action. (D) The efforts by the Administrator to protect privacy and civil liberties with respect to the following: (i) The actions that may be taken pursuant to subsection (a). (ii) The actions that may be taken pursuant to subsection (a) of section 50925. (i) Definitions In this section: (1) Covered facility The term covered facility means any facility that satisfies the following requirements: (A) Is under the jurisdiction of the Administration. (B) Is identified by the Administrator as a facility critical to a function of the Administration. (2) Local law enforcement agency The term local law enforcement agency means the law enforcement agency of a county or county-equivalent entity. (3) Specified entities The term specified entities means the following: (A) The Committee on Energy and Commerce and the Committee on Science, Space, and Technology of the House of Representatives. (B) The Committee on Commerce, Science, and Transportation of the Senate. (C) The Attorney General. (D) The Secretary of Defense. (E) The Secretary of Homeland Security. (F) The Administrator of the Federal Aviation Administration. (4) Unmanned aircraft; unmanned aircraft system The terms unmanned aircraft and unmanned aircraft system have the meanings given such terms in section 44801 of title 49. .\n**(2) Clerical amendment**\nThe table of sections for chapter 201 of title 51, United States Code, is amended by inserting after the item relating to section 20117 the following new item:\n20118. Authority to take actions to protect certain NASA facilities and assets from unmanned aircraft .\n##### (b) Authority To protect space launch property from unmanned aircraft\n**(1) In general**\nChapter 509 of title 51, United States Code, is amended by adding at the end the following new section:\n50925. Authority to take actions to protect space launch property from unmanned aircraft (a) Authority Subject to section 20118 and notwithstanding any other provision of law, a covered entity may take, and may authorize officers and employees of such entity to take, such actions as are described in subsection (b) that are necessary to mitigate the threat an unmanned aircraft system or unmanned aircraft poses to the safety or security of the covered property of such entity. (b) Actions described The actions described in this subsection are the following: (1) Detect, identify, monitor, and track an unmanned aircraft system or unmanned aircraft, without prior consent. (2) Warn the operator of such unmanned aircraft system or unmanned aircraft, as the case may be. (3) Disrupt control of such unmanned aircraft system or unmanned aircraft, as the case may be, without prior consent, including by disabling such unmanned aircraft system or unmanned aircraft, as the case may be, by intercepting electronic communications or otherwise interfering with such communications. (4) Seize or exercise control of such unmanned aircraft system or unmanned aircraft, as the case may be. (5) Seize or otherwise confiscate such unmanned aircraft system or unmanned aircraft, as the case may be. (6) Use reasonable force to disable, damage, or destroy such unmanned aircraft system or unmanned aircraft, as the case may be. (c) Forfeiture Any unmanned aircraft system or unmanned aircraft described in subsection (a) and seized by a covered entity is subject to forfeiture to the local law enforcement agency for the jurisdiction in which such unmanned aircraft system or unmanned aircraft, as the case may be, was so seized. (d) Signage A covered entity shall display on each covered property of such entity a sign that includes information relating to the following: (1) The actions that may be taken pursuant to subsection (a). (2) Forfeiture under subsection (c). (e) Determination Each year, a covered entity shall consult with each local law enforcement agency for the covered property of such entity to determine the most effective and least hazardous means to take actions pursuant to subsection (a). (f) Liability If an unmanned aircraft system or unmanned aircraft poses a threat described in subsection (a) and an action is taken pursuant to such subsection to mitigate such threat, the operator of such unmanned aircraft system or unmanned aircraft, as the case may be, is liable for damages caused by such action. (g) Reports Not later than 30 days after an instance in which an action described in paragraphs (3) through (6) of subsection (b) is taken pursuant to subsection (a), the covered entity through which such action was so taken shall carry out the following: (1) Submit to the local law enforcement agency for the jurisdiction in which such action was so taken a report on such instance that satisfies the following requirements: (A) Is in a form specified by such agency. (B) Includes information relating to the justification for so taking such action. (2) Submit to the Administrator a report on such instance that satisfies the following requirements: (A) Is in a form specified by the Administrator. (B) Includes information relating to such justification. (C) Includes an identification of the means through which such action was so taken. (h) Definitions In this section: (1) Covered entity The term covered entity means a person or entity licensed under this chapter to conduct launch, reentry, testing, or manufacturing activities. (2) Covered property The term covered property means any real property, including airspace over such property, that is owned, leased, or under the control of a covered entity and is a site where launch, reentry, testing, or manufacturing activities occur. (3) Local law enforcement agency The term local law enforcement agency means the law enforcement agency of a county or county-equivalent entity. (4) Unmanned aircraft; unmanned aircraft system The terms unmanned aircraft and unmanned aircraft system have the meanings given such terms in section 44801 of title 49. .\n**(2) Clerical amendment**\nThe table of sections for chapter 509 of title 51, United States Code, is amended by adding at the end the following new item:\n50925. Authority to take actions to protect space launch property from unmanned aircraft .",
      "versionDate": "2026-04-22",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8458ih.xml"
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
      "title": "STAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Theft and Aerospace Reconnaissance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 51, United States Code, to authorize certain actions to protect certain facilities and assets from unmanned aircraft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:21Z"
    }
  ]
}
```
