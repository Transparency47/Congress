# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3641
- Title: No Relief for Allies of Dictators Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3641
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-02-09T19:29:16Z
- Update date including text: 2026-02-09T19:29:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3641",
    "number": "3641",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "No Relief for Allies of Dictators Act of 2026",
    "type": "S",
    "updateDate": "2026-02-09T19:29:16Z",
    "updateDateIncludingText": "2026-02-09T19:29:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T20:03:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3641is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3641\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Scott of Florida (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo revoke the visas of, and impose visa restrictions on, certain individuals located in the United States and abroad who are associated with regimes in Venezuela, Cuba, Nicaragua, and Bolivia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Relief for Allies of Dictators Act of 2026 .\n#### 2. Visa restrictions for certain Venezuelans, Cubans, Nicaraguans, and Bolivians\n##### (a) In general\nThe Secretary of State shall revoke the visa of, or impose visa restrictions on, any individual described in subsection (b) who the Secretary determines\u2014\n**(1)**\n**(A)**\nis responsible for, is complicit in, is responsible for ordering, controlling, or otherwise directing, or is knowingly\u2014\n**(i)**\ncommitting human rights violations at any time in Venezuela, Cuba, Nicaragua, or Bolivia; or\n**(ii)**\nparticipating in (directly or indirectly) any activity in or in relation to Venezuela, Cuba, Nicaragua, or Bolivia at any time that undermines or threatens the integrity of the democracy or sovereignty of, the people of Cuba, Venezuela, Nicaragua, or Bolivia; or\n**(B)**\nis the spouse or child of a foreign person described in subparagraph (A); or\n**(2)**\n**(A)**\nis described in or identified under\u2014\n**(i)**\nsection 804(b) of the Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1903(b) );\n**(ii)**\nExecutive Order 13850 (83 Fed. Reg. 55243; relating to blocking property of additional persons contributing to the situation in Venezuela); or\n**(iii)**\nExecutive Order 13884 (84 Fed. Reg. 38843; relating to blocking property of the Government of Venezuela); or\n**(B)**\nis the spouse or child of a foreign person described in subparagraph (A).\n##### (b) Individual described\nAn individual described in this subsection is any foreign person, located in the United States or abroad, who\u2014\n**(1)**\nwith respect to Venezuela, is\u2014\n**(A)**\na former official of the Hugo Chavez regime; or\n**(B)**\na current or former official of the Nicolas Maduro regime;\n**(2)**\nwith respect to Cuba, is\u2014\n**(A)**\na former official of the Fidel Castro or Raul Castro regime; or\n**(B)**\na current or former official of the Miguel Diaz-Canel regime;\n**(3)**\nwith respect to Nicaragua, is\u2014\n**(A)**\na current or former official of the Daniel Ortega regime; or\n**(B)**\na Sandinista party member;\n**(4)**\nwith respect to Bolivia, is a former official of the Evo Morales regime;\n**(5)**\nacts on behalf of a regime or party described in any of paragraphs (1) through (4);\n**(6)**\naids in repression by such regime or party; or\n**(7)**\nassists such regime or party.\n##### (c) Visa restrictions described\n**(1) Exclusion from the United States and revocation of visa or other documentation**\nAn individual described in subsection (b)\u2014\n**(A)**\nis inadmissible to the United States;\n**(B)**\nis ineligible to receive a visa or other documentation authorizing entry into the United States;\n**(C)**\nis otherwise ineligible to be admitted or paroled into the United States or to receive any benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ); and\n**(D)**\nshall\u2014\n**(i)**\nin accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), have his or her visa or other documentation revoked, regardless of when the visa or other documentation was issued; and\n**(ii)**\nbe subject to expedited removal.\n**(2) Applicability for individuals visiting United Nations headquarters**\nIn the case of an individual described in subsection (b) who intends to travel to the United States to visit the headquarters of the United Nations, the Secretary of State, in consultation with the Director of National Intelligence, the Attorney General, and the Secretary of Homeland Security, shall make a case-by-case determination with respect to the applicability of subsection (a) to such individual.\n##### (d) Rulemaking\nThe President shall issue such regulations, licenses, and orders as may be necessary to carry out this section.",
      "versionDate": "2026-01-14",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-09T19:29:16Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3641is.xml"
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
      "title": "No Relief for Allies of Dictators Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Relief for Allies of Dictators Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to revoke the visas of, and impose visa restrictions on, certain individuals located in the United States and abroad who are associated with regimes in Venezuela, Cuba, Nicaragua, and Bolivia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:31Z"
    }
  ]
}
```
