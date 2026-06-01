# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1854?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1854
- Title: Haiti Criminal Collusion Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1854
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-11-01T03:53:14Z
- Update date including text: 2025-11-01T03:53:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 233.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 233.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1854",
    "number": "1854",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Haiti Criminal Collusion Transparency Act of 2025",
    "type": "S",
    "updateDate": "2025-11-01T03:53:14Z",
    "updateDateIncludingText": "2025-11-01T03:53:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 233.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
        "item": [
          {
            "date": "2025-10-30T15:02:27Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:37Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T22:10:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "VA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "UT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1854is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1854\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mrs. Shaheen (for herself, Mr. Scott of Florida , Mr. Kaine , Mr. Curtis , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo required the imposition of sanctions with respect to political and economic elites in Haiti, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Haiti Criminal Collusion Transparency Act of 2025 .\n#### 2. Reporting requirements\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in coordination with other Federal agencies as the Secretary determines appropriate, shall submit to the appropriate congressional committees a report on the connections between criminal gangs and political elites and economic elites in Haiti.\n##### (b) Contents\nThe report required by subsection (a) shall include\u2014\n**(1)**\na list identifying prominent criminal gangs in Haiti, including\u2014\n**(A)**\nthe leaders of each gang;\n**(B)**\na description of the criminal activities of each gang, including coercive recruitment; and\n**(C)**\nthe primary geographic area of operations for each gang;\n**(2)**\na list of political elites and economic elites in Haiti who knowingly have direct and significant links to criminal gangs and any organizations or entities controlled by such political elites and economic elites;\n**(3)**\na detailed description of the relationship between the political elites and economic elites listed pursuant to paragraph (2) and the criminal gangs identified pursuant to paragraph (1);\n**(4)**\na detailed description of how political elites and economic elites in Haiti use relationships with criminal gangs to advance political and economic interests and agendas;\n**(5)**\na list of each criminal organization assessed to be trafficking Haitians and other individuals to the United States border;\n**(6)**\nan assessment of connections between political elites and economic elites, criminal gangs in Haiti, and transnational criminal organizations;\n**(7)**\nan assessment of how the nature and extent of collusion between political elites and economic elites and criminal gangs threatens the people of Haiti and the national interests and activities of the United States in Haiti; and\n**(8)**\nan assessment of potential actions that the Government of the United States and the Government of Haiti could take to address the findings made pursuant to paragraph (6).\n##### (c) Form of report\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n#### 3. Sanctions\n##### (a) In general\nNot later than 90 days after the date the report required by section 2 is submitted to the appropriate congressional committees, the President shall impose sanctions described in subsection (b) with respect to each foreign person identified pursuant to paragraphs (1) and (2) of section 2(b).\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Property blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of any foreign person described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Aliens inadmissible for visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subsection (a) regardless of when the visa or other entry documentation was issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices to Haiti;\n**(B)**\nthe provision of humanitarian assistance to the people of Haiti;\n**(C)**\nfinancial transactions relating to humanitarian assistance or for humanitarian purposes in Haiti; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance or humanitarian purposes in Haiti.\n##### (d) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person that violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n##### (e) Waiver\nThe President may waive the application of sanctions imposed with respect to a foreign person under this section if the President certifies to the appropriate congressional committees, not later than 15 days before such waiver takes effect, that the waiver is vital to the national security interests of the United States.\n#### 4. Definitions\nIn this Act:\n**(1) Admitted; alien; lawfully admitted for permanent residence**\nThe terms admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(4) Economic elite**\nThe term economic elite means a board member, officer, or executive of a group, committee, corporation, or other entity that exerts substantial influence or control over the economy, infrastructure, or a particular industry of Haiti.\n**(5) Political elite**\nThe term political elite means a current or former government official, or the high-level staff of any such government official, a political party leader, or a political committee leader of Haiti.\n**(6) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States; or\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 5. Sunset\nThis Act shall cease to have any force or effect beginning on the date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1854rs.xml",
      "text": "II\nCalendar No. 233\n119th CONGRESS\n1st Session\nS. 1854\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mrs. Shaheen (for herself, Mr. Scott of Florida , Mr. Kaine , Mr. Curtis , Mr. Coons , Mr. Booker , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo required the imposition of sanctions with respect to political and economic elites in Haiti, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Haiti Criminal Collusion Transparency Act of 2025 .\n#### 2. Reporting requirements\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in coordination with other Federal agencies as the Secretary determines appropriate, shall submit to the appropriate congressional committees a report on the connections between criminal gangs and political elites and economic elites in Haiti.\n##### (b) Contents\nThe report required by subsection (a) shall include\u2014\n**(1)**\na list identifying prominent criminal gangs in Haiti, including\u2014\n**(A)**\nthe leaders of each gang;\n**(B)**\na description of the criminal activities of each gang, including coercive recruitment; and\n**(C)**\nthe primary geographic area of operations for each gang;\n**(2)**\na list of political elites and economic elites in Haiti who knowingly have direct and significant links to criminal gangs and any organizations or entities controlled by such political elites and economic elites;\n**(3)**\na detailed description of the relationship between the political elites and economic elites listed pursuant to paragraph (2) and the criminal gangs identified pursuant to paragraph (1);\n**(4)**\na detailed description of how political elites and economic elites in Haiti use relationships with criminal gangs to advance political and economic interests and agendas;\n**(5)**\na list of each criminal organization assessed to be trafficking Haitians and other individuals to the United States border;\n**(6)**\nan assessment of connections between political elites and economic elites, criminal gangs in Haiti, and transnational criminal organizations;\n**(7)**\nan assessment of how the nature and extent of collusion between political elites and economic elites and criminal gangs threatens the people of Haiti and the national interests and activities of the United States in Haiti; and\n**(8)**\nan assessment of potential actions that the Government of the United States and the Government of Haiti could take to address the findings made pursuant to paragraph (6).\n##### (c) Form of report\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n#### 3. Sanctions\n##### (a) In general\nNot later than 90 days after the date the report required by section 2 is submitted to the appropriate congressional committees, the President shall impose sanctions described in subsection (b) with respect to each foreign person identified pursuant to paragraphs (1) and (2) of section 2(b).\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Property blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of any foreign person described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Aliens inadmissible for visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subsection (a) regardless of when the visa or other entry documentation was issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices to Haiti;\n**(B)**\nthe provision of humanitarian assistance to the people of Haiti;\n**(C)**\nfinancial transactions relating to humanitarian assistance or for humanitarian purposes in Haiti; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance or humanitarian purposes in Haiti.\n##### (d) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person that violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n##### (e) Waiver\nThe President may waive the application of sanctions imposed with respect to a foreign person under this section if the President certifies to the appropriate congressional committees, not later than 15 days before such waiver takes effect, that the waiver is vital to the national security interests of the United States.\n#### 4. Definitions\nIn this Act:\n**(1) Admitted; alien; lawfully admitted for permanent residence**\nThe terms admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(4) Economic elite**\nThe term economic elite means a board member, officer, or executive of a group, committee, corporation, or other entity that exerts substantial influence or control over the economy, infrastructure, or a particular industry of Haiti.\n**(5) Political elite**\nThe term political elite means a current or former government official, or the high-level staff of any such government official, a political party leader, or a political committee leader of Haiti.\n**(6) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States; or\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 5. Sunset\nThis Act shall cease to have any force or effect beginning on the date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
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
        "updateDate": "2025-06-20T12:51:09Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1854is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1854rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Haiti Criminal Collusion Transparency Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:14Z"
    },
    {
      "title": "Haiti Criminal Collusion Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to required the imposition of sanctions with respect to political and economic elites in Haiti, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-31T10:56:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Haiti Criminal Collusion Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    }
  ]
}
```
