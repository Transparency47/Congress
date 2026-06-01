# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6736
- Title: ARMAS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6736
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-05-15T08:07:44Z
- Update date including text: 2026-05-15T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6736",
    "number": "6736",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001091",
        "district": "20",
        "firstName": "Joaquin",
        "fullName": "Rep. Castro, Joaquin [D-TX-20]",
        "lastName": "Castro",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "ARMAS Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:44Z",
    "updateDateIncludingText": "2026-05-15T08:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CT"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "RI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "WA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "AZ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MN"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NV"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "DC"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6736ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6736\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Castro of Texas (for himself, Mrs. Torres of California , Mr. Goldman of New York , Mrs. Cherfilus-McCormick , Ms. DeLauro , Mr. Magaziner , Ms. Vel\u00e1zquez , Mr. Frost , Ms. Dean of Pennsylvania , Mrs. Ramirez , Ms. Jayapal , Mrs. Grijalva , Ms. Omar , Mr. McGovern , Ms. Kelly of Illinois , Ms. Wasserman Schultz , Mr. Menendez , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the transfer of regulatory control of certain munitions exports from the Department of Commerce to the Department of State, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Americas Regional Monitoring of Arms Sales Act of 2025 or the ARMAS Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Findings.\nSec.\u20023.\u2002Transfer of regulatory control of certain munitions exports from Department of Commerce to Department of State.\nSec.\u20024.\u2002Reports and strategy on disruption of illegal export and trafficking of firearms to Mexico and certain Central American and Caribbean countries.\nSec.\u20025.\u2002Increasing participation in the eTrace program.\nSec.\u20026.\u2002Modifications to the Caribbean Basin Security Initiative.\nSec.\u20027.\u2002Designation of covered countries.\nSec.\u20028.\u2002Certification requirements relating to certain munitions exports.\nSec.\u20029.\u2002Limitation on licenses and other authorizations for export of certain items removed from the Commerce Control List and included on the United States Munitions List.\nSec.\u200210.\u2002Prohibition on promotion of covered munitions.\nSec.\u200211.\u2002Definitions.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nViolence in Mexico, Central America, and the Caribbean is exacerbated by firearms originating in the United States.\n**(2)**\nWhile firearms are trafficked to Mexico from a variety of countries, firearms originating in the United States account for 70 percent of the firearms recovered and traced from crimes in Mexico, according to the 2021 Government Accountability Office (GAO) report published by the Comptroller General of the United States titled Firearms Trafficking: U.S. Efforts to Disrupt Gun Smuggling into Mexico Would Benefit from Additional Data and Analysis .\n**(3)**\nUnited States-origin firearm flows contribute to human rights violations, organized crime and gang violence, extrajudicial killings, high homicide rates, domestic violence, and femicides in Mexico, Central America, and the Caribbean.\n**(4)**\nFirearms trafficking from the United States and firearm violence are key drivers of immigration and asylum claims from Central America.\n**(5)**\nAccording to the United Nations Regional Centre for Peace, Disarmament and Development in Latin America and the Caribbean, firearms are used in 70 percent of homicides in the Caribbean compared to 30 percent globally, and while the Caribbean constitutes less than one percent of the global population, it is responsible for 23 percent of all recorded homicides.\n**(6)**\nIn an August 2022 press conference, United States officials of Homeland Security Investigations reported a marked uptick in the number of weapons , and an increase in the caliber and type of weapons, being illegally trafficked to Haiti and the rest of the Caribbean.\n**(7)**\nThe Caribbean Basin Security Initiative of the Department of State that commenced in 2009 is the regional foreign assistance program of the United States that seeks to reduce illicit trafficking in the Caribbean region and advance public safety and security. The program includes improving the capacity of Caribbean countries to intercept smuggled weapons at airports and seaports, as well as support for forensic ballistics and firearms destruction and stockpile management. Assistance under the Caribbean Basin Security Initiative has also included support for regional organizations, including\u2014\n**(A)**\nthe Caribbean Community Implementation Agency for Crime and Security (CARICOM IMPACS), based in Trinidad and Tobago, the lead agency involved in the issue of illicit firearms trafficking and increasing the capacity of member states to detect and prevent firearms trafficking; and\n**(B)**\nthe Eastern Caribbean\u2019s Regional Security System, based in Barbados.\n**(8)**\nTwo GAO reports (published in 2021 and 2022, respectively) on firearms trafficking have affirmed that firearms trafficking to Mexico and Central America continues to represent a security concern to the United States, as United States-origin firearms are diverted from legitimate owners and end up in the hands of violent criminals, including drug traffickers and other transnational criminal organizations. A GAO report on the effect of firearms trafficking in the Caribbean has not yet been compiled.\n**(9)**\nIn these reports, the Comptroller General found that Federal departments and agencies lacked information and analysis of the firearms trafficking networks in Mexico and Central America, that few efforts of the United States Government in the region focused on firearms trafficking, and that, as a result, such agencies lack a detailed understanding of the firearms trafficking that fuels violence and enables criminals in Belize, El Salvador, Guatemala, Honduras, and Mexico.\n**(10)**\nFirearms used to kidnap and kill a group of United States citizens traveling in Matamoros, Mexico were illegally smuggled from the United States into Mexico. The suspect in these killings admitted to Federal agents that he purchased firearms in the United States, smuggled them across the border, and knowingly provided them to members of the Gulf Cartel.\n**(11)**\nAs the incident specified in paragraph (11) demonstrates, United States-sourced firearms are being smuggled and diverted to cartels implicated in the supply and flow of illegal fentanyl and other dangerous drugs, threatening the public health and safety of United States citizens.\n**(12)**\nIn the 2022 GAO report Firearms Trafficking: More Information Needed to Inform U.S. Efforts in Central America , the Comptroller General found that efforts of the United States Government focused on firearms trafficking in Belize, El Salvador, Guatemala, and Honduras lacked information about relevant country conditions and performance measures to ensure such efforts were designed and implemented to achieve the intended objectives and, as a result, the Comptroller General recommended that the Secretary of State obtain information about the conditions in such countries, to support the development of effective programs to reduce the availability of illicit firearms.\n**(13)**\nData on firearms trafficking is limited and to understand the problem, data compilation is crucial.\n**(14)**\nAs of the date of the publication of the report specified in paragraph (12), the Secretary of Commerce had not assigned any agents to Central America on permanent assignment.\n**(15)**\nIn 2021 and 2022, the annual Country Reports on Human Rights Practices of the Department of State included unlawful and arbitrary killings as a significant human rights issue in Guatemala, yet despite such inclusion, the Under Secretary of Commerce for Industry and Security has authorized approximately 99,270 firearms exports to Guatemala since assuming responsibility for firearms licensing in 2020.\n**(16)**\nWhen firearms were controlled under the United States Munitions List and the licensing of firearms was the responsibility of the Secretary of State, the average number of firearms licensed for export to Guatemala was approximately 4,000 per year.\n**(17)**\nThe current number of exports specified in paragraph (15) represents an extraordinary increase (as much as 25 times the average) from the number specified in paragraph (16), and the Under Secretary of Commerce for Industry and Security has only been able to conduct a very limited number of end-use checks, according to the 2022 GAO report Firearms Trafficking: More Information Needed to Inform U.S. Efforts in Central America .\n**(18)**\nSince the Department of Commerce gained jurisdiction over the control of firearm export licensing, there has been a 30 percent increase in firearm exports in comparison to averages for such exports when the control of such exports was under the jurisdiction of the Department of State. The Secretary of Commerce has also approved 95 percent of license applications for such exports.\n**(19)**\nAccording to the U.S. Census Bureau, Mexico, Guatemala, and Brazil have been among the top 10 destinations for United States-manufactured semiautomatic firearm exports.\n**(20)**\nThe Bipartisan Safer Communities Act ( Public Law 117\u2013159 ), which was enacted into law on June 25, 2022, implemented key efforts to address firearm trafficking, including by establishing a Federal criminal offense for firearm trafficking and by strengthening the capability of the Bureau of Alcohol, Tobacco, Firearms and Explosives to interdict firearms.\n**(21)**\nA growing number of firearms exported by United States manufacturers are found involved in violent crimes worldwide. For instance, the pistol used in a mass shooting of 23 children and two teachers in Thailand in October 2022 was linked to a United States factory.\n#### 3. Transfer of regulatory control of certain munitions exports from Department of Commerce to Department of State\n##### (a) Transfer\nNot later than 1 year after the date of the enactment of this Act\u2014\n**(1)**\nthe Secretary of Commerce shall transfer the control over the export of each previously covered item to the jurisdiction of the Department of State; and\n**(2)**\nfollowing such transfer, the Secretary of State may not transfer the control over the export of any covered munition to the jurisdiction of the Department of Commerce.\n##### (b) Regulations\nThe Secretary of State and the Secretary of Commerce shall prescribe such regulations as may be necessary to implement this section by the date specified in subsection (a).\n##### (c) Rule of construction\nNothing in this section shall be construed as limiting any authority relating to the designation, control, or removal of items under the United States Munitions List or the Commerce Control List, other than the specific authority to transfer the control of an item as specified in subsection (a).\n##### (d) Prohibition on promotion of certain munitions exports by Department of Commerce\nThe Secretary of Commerce may not take any actions to promote the export of any previously covered item, including actions before, on, or after the date on which the Secretary transfers the control over the export of the previously covered item to the jurisdiction of the Department State under subsection (a).\n#### 4. Reports and strategy on disruption of illegal export and trafficking of firearms to Mexico and certain Central American and Caribbean countries\n##### (a) Report\n**(1) Submission**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State (in consultation with the Secretary of Commerce, the Attorney General, the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, and the heads of such other Federal departments or agencies as the Secretary of State may determine relevant) shall submit to the appropriate congressional committees a report on the efforts of the Secretary of State and the heads of other relevant Federal departments and agencies to disrupt the following:\n**(A)**\nThe illegal export or diversion of firearms from the United States to unauthorized recipients in countries designated as covered countries under section 7 (including through unauthorized third-party transfers).\n**(B)**\nThe illegal trafficking of firearms obtained in the United States to recipients in such countries.\n**(2) Matters**\nThe report under paragraph (1) shall include, with respect to the efforts specified in such paragraph, the following:\n**(A)**\nAn identification of any such efforts, including efforts to accomplish the following objectives:\n**(i)**\nTracking and verifying information regarding the end-users of firearms so exported, including by entering into data-sharing agreements\u2014\n**(I)**\nwith appropriate counterparts from the governments of such covered countries; and\n**(II)**\nbetween the relevant departments and agencies of the United States Government.\n**(ii)**\nEnsuring the destruction of surplus firearms so exported.\n**(iii)**\nEnsuring that firearms so exported are not used to commit extrajudicial killings or other gross violations of internationally recognized human rights.\n**(iv)**\nBuilding the capacity of such covered countries to prevent the trafficking of firearms so exported, including through current programs supported or implemented by the United States Government.\n**(v)**\nTracking and verifying information regarding the end-users of firearms obtained in the United States and illegally trafficked to such covered countries.\n**(vi)**\nCombating all forms of cross-border smuggling of firearms from the United States, including via maritime vessels and aircraft.\n**(vii)**\nEngaging with subnational government officials in such covered countries to effectively implement and enforce agreements relating to the trafficking of firearms that have been concluded between the United States Government and the national government of the respective covered country.\n**(viii)**\nIdentifying the origin of trafficked firearms, including through the serial numbers of trafficked firearms, and sharing such information with relevant law enforcement agencies of\u2014\n**(I)**\nthe United States;\n**(II)**\nthe respective covered country; and\n**(III)**\nany other country determined relevant for purposes of such information sharing.\n**(ix)**\nImplementing the proposed security cooperation plan titled U.S.-Mexico Bicentennial Framework for Security, Public Heath, and Safe Communities , and any successor or subsequent bilateral agreements on combating firearm trafficking, transnational organizations, or fentanyl.\n**(x)**\nCooperating with other relevant Federal departments and agencies, including the Attorney General, the Secretary of Homeland Security, and the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, to combat firearms trafficking and prosecute illegal firearm smugglers.\n**(B)**\nAn assessment of the results of the efforts identified pursuant to subparagraph (A).\n**(C)**\nA description of how homicides, extrajudicial killings, and other gross violations of internationally recognized human rights committed in such covered countries using firearms exported from or obtained in the United States have been investigated.\n##### (b) Inter-Agency strategy\n**(1) In general**\nThe Secretary of State, in consultation with the Secretary of Commerce, taking into account the findings of the report under subsection (a), shall jointly develop an inter-agency strategy for the disruption of the trafficking of firearms exported from the United States to recipients in countries designated as covered countries under section 7 .\n**(2) Elements**\nThe strategy under paragraph (1) shall include the following:\n**(A)**\nA plan for the United States to accomplish each of the objectives specified in subsection (a)(2)(A).\n**(B)**\nAn identification of specific performance measures, targets (including the baselines for such targets), and timelines with respect to such objectives.\n**(C)**\nAn estimate of the resources and personnel necessary to carry out the strategy.\n**(D)**\nA plan for cooperation between the Secretary of State, the Secretary of Commerce, and the heads of any other Federal departments or agencies involved in anti-firearm trafficking efforts, including the Attorney General, the Secretary of Homeland Security, and the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives.\n**(E)**\nA plan for coordination between the Secretary of State, the Secretary of Commerce, and such heads regarding efforts in countries designated as covered countries under section 7 to combat the trafficking of United States-sourced firearms\u2014\n**(i)**\nfrom the United States to such designated countries; and\n**(ii)**\nfrom such designated countries to other countries in the surrounding region.\n**(3) Required considerations; consultations**\nIn developing the strategy under paragraph (1), the Secretary of State shall\u2014\n**(A)**\nconsider how the strategy may support or otherwise align with broader efforts of the Secretary of State relating to security assistance, anti-corruption, and the prevention of organized crime and drug and gang violence;\n**(B)**\nconsider whether the placement in the Western Hemisphere of an export control officer of the Bureau of Industry and Security of the Department of Commerce, or other personnel of the Department of Commerce or the Department of State, would support the strategy; and\n**(C)**\nseek to consult with appropriate counterparts from the government of each country designated as a covered country under section 7 .\n**(4) Submission to Congress**\nNot later than January 1 of the year following the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees the strategy under paragraph (1).\n##### (c) Improved tracking of trafficked firearms\n**(1) Assessment of data availability**\nNot later than 180 days after the date on which a country is designated (or the deemed to be designated, as the case may be), under section 7 , the Secretary of State, in consultation with the Secretary of Commerce, the Attorney General, the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, and the heads of such other Federal departments or agencies as the Secretary of State may determine relevant, shall conduct and submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate an assessment of the extent to which the law enforcement agencies of that designated country make available to the United States Government forensic information of trafficked firearms.\n**(2) Addressing gaps in data**\nFor the duration of the period during which a country is designated as a covered country under section 7 , the Secretary of State shall\u2014\n**(A)**\nseek to engage with the foreign counterparts of the government of such country to improve the collection and sharing of the forensic information of trafficked firearms confiscated by the law enforcement agencies of such country; and\n**(B)**\npromptly provide any such forensic information shared pursuant to subparagraph (A) to the relevant Federal, State, and local law enforcement agencies for purposes of use in criminal or civil investigations into violations of relevant United States Federal laws, including the Arms Export Control Act.\n**(3) Forensic information defined**\nIn this subsection, the term forensic information , with respect to a trafficked firearm, includes\u2014\n**(A)**\nthe serial number of the firearm; and\n**(B)**\nany other information that may be used to identify the origin of the firearm or any person or organization involved in the trafficking of the firearm.\n##### (d) Annual report\n**(1) Submission**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary or Secretaries concerned (in consultation with the heads of such other Federal departments or agencies as the Secretary or Secretaries concerned may determine relevant) shall submit to the appropriate congressional committees a report on the export of covered munitions to countries designated as covered countries under section 7 .\n**(2) Matters**\nEach report under paragraph (1) shall include, with respect to the year for which the report is submitted, the following information (disaggregated by country):\n**(A)**\nInformation regarding license applications approved or denied, and previously issued licenses modified or revoked, for the export of covered munitions to proposed recipients in covered countries.\n**(B)**\nInformation regarding how evolving country contexts, including with respect to developments in human rights, affected the approval of license applications for such exports.\n**(C)**\nThe number of licenses issued for the export of covered munitions to proposed recipients in covered countries.\n**(D)**\nThe number of covered munitions exported to recipients in covered countries.\n**(E)**\nWith respect to end-user checks for covered munitions exported to recipients in covered countries under section 38(g)(7) of the Arms Export Control Act ( 22 U.S.C. 2778(g)(7) ) (commonly referred to as the Blue Lantern program), the monitoring program established under the second section 40A of the Arms Export Control Act ( 22 U.S.C. 2785 ) (as added by section 150(a) of Public Law 104\u2013164 ), or other applicable programs of the Department of Commerce or Department of State, the following information:\n**(i)**\nThe number of such end-user checks requested.\n**(ii)**\nThe number of such end-user checks conducted.\n**(iii)**\nThe type of such end-user checks conducted.\n**(iv)**\nThe results of such end-user checks conducted.\n**(F)**\nInformation on the extent to which the heads of the governments of covered countries shared with the Secretary or Secretaries concerned and the heads of other relevant Federal departments and agencies (such as the Bureau of Alcohol, Tobacco, Firearms and Explosives) data relating to the receipt and end-use of covered munitions exported from the United States, and the type of data so shared.\n**(G)**\nFor each covered country, a description of the United States funding and resources allocated for the purpose of disrupting trafficking of covered munitions.\n**(3) Secretary or Secretaries concerned defined**\nIn this subsection, the term Secretary or Secretaries concerned means\u2014\n**(A)**\nif a single Federal department or agency has jurisdiction over the export control of covered munitions, the Secretary of that Federal department or agency; or\n**(B)**\nif multiple Federal departments or agencies have jurisdiction over the export control of covered munitions, each Secretary of such a Federal department or agency.\n#### 5. Increasing participation in the eTrace program\n##### (a) In general\nThe Secretary of State, in coordination with the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, shall seek to work with national and sub-national law enforcement authorities of countries designated as covered countries under section 7 in order to increase participation by such authorities in the eTrace program.\n##### (b) Report\nNot later than 2 years after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on the implementation of subsection (a) and on the number of firearms traced to a purchase or export that resulted in Federal investigations and prosecutions.\n##### (c) Haiti\nThe Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives shall ensure that the eTrace program is available in the French and Haitian Creole languages for the purposes of improving the use of the program by law enforcement authorities in Haiti.\n##### (d) Authorization of appropriation\nAmounts authorized to be appropriated under chapter 8 of part I of the Foreign Assistance Act of 1961 (relating to international narcotics control assistance) are authorized to be made available to carry out this section.\n##### (e) Definition of eTrace program\nIn this section, the term eTrace program means the web-based firearms tracing system of the Bureau of Alcohol, Tobacco, Firearms and Explosives that is available to accredited domestic and international law enforcement agencies to assist in the tracing of United States-sourced firearms.\n#### 6. Modifications to the Caribbean Basin Security Initiative\nThe Secretary of State shall update the Caribbean Basin Security Initiative\u2019s Results Framework to establish specific indicators relating to trafficking in firearms.\n#### 7. Designation of covered countries\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall designate each country that the Secretary determines meets the requirements under subsection (b) as a covered country for purposes of this Act.\n##### (b) Requirements\nA country meets the requirements under this subsection if the country\u2014\n**(1)**\nis located in North America, South America, or the Caribbean;\n**(2)**\nis not a member state of the North Atlantic Treaty Organization; and\n**(3)**\nmeets such other requirements as the Secretary may determine appropriate.\n##### (c) Initial designations\nThe Bahamas, Belize, Brazil, Colombia, El Salvador, Guatemala, Honduras, Mexico, Haiti, Jamaica, and Trinidad and Tobago\u2014\n**(1)**\nshall be deemed to have been so designated by the Secretary of State as of the date of the enactment of this Act; and\n**(2)**\nshall continue to be deemed so designated for a five-year period, during which time the designation may not be terminated under subsection (d).\n##### (d) Termination of designation\nSubject to subsection (c)(2), the Secretary of State may terminate the designation of a country under this section only if, at least 180 days prior to such termination, the Secretary submits to the appropriate congressional committees a notification of such termination.\n#### 8. Certification requirements relating to certain munitions exports\n##### (a) Initial certification; prohibition\n**(1) In general**\nExcept as provided in paragraph (2), no covered munition may be transferred to the government of a country designated as a covered country under section 7, or any other organization, citizen, or resident of such covered country, until the Secretary of State submits to the appropriate congressional committees a certification that the program required under subsection (c) has been established.\n**(2) Waiver**\nFor the one-year period beginning on the effective date of this section described in subsection (d), the Secretary of State may waive the certification requirement under paragraph (1) with respect to the transfer of a covered munition to the government of a country described in paragraph (1) if the Secretary certifies to the appropriate congressional committees that such waiver is in the national security interest of the United States and includes a written justification with the certification.\n##### (b) Review and recertification\n**(1) In general**\nNot later than 3 years after the date of the submission of the certification under subsection (a) for a country designated as a covered country under section 7, and annually thereafter until such time as the designation is terminated, the Secretary of State shall review, and submit to the appropriate congressional committees a recertification of, such certification.\n**(2) Prohibition**\nIf the Secretary of State is unable to recertify a covered country as required under paragraph (1), no covered munition may be transferred to the government of the covered country, or any other organization, citizen, or resident of such covered country, until the date on which the Secretary is able to so recertify.\n##### (c) Program\n**(1) Establishment**\nThe Secretary of State shall establish and carry out a program under which the Secretary shall prohibit the retransfer of covered munitions transferred to countries designated as covered countries under section 7without the consent of the United States and provide for the registration and end-use monitoring of such covered munitions in accordance with the following requirements:\n**(A)**\nThe maintenance of a detailed record of the origin, shipping, and distribution of covered munitions transferred to countries designated as covered countries under section 7.\n**(B)**\nThe registration of the serial numbers of all covered munitions, to be provided to the governments of such covered countries and other organizations, citizens, and residents within such covered countries.\n**(C)**\nThe conduct of a program for the end-use monitoring of covered munitions transferred to the entities and individuals described in subparagraph (B).\n**(2) Review of database**\nIn prohibiting the retransfer of covered munitions without the consent of the United States pursuant to the program under paragraph (1), the Secretary of State, in consultation with the Secretary of Commerce, shall\u2014\n**(A)**\nreview the database of the Department of State that stores records relating to vetting conducted pursuant to section 620M of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2378d ) or section 362 of title 10, United States Code, known as the International Vetting and Security Tracking-cloud system or INVEST system (or any successor database), for any such records relating to the prospective recipients of such retransfer; and\n**(B)**\nensure that such consent is not granted for any such prospective recipient who the Secretary of State determines, taking into account the review under subparagraph (A), is credibly implicated in a gross violation of internationally recognized human rights.\n**(3) Data storage and sharing**\nIn carrying out the program under paragraph (1), the Secretary of State shall\u2014\n**(A)**\nensure that any data received pursuant to such program is stored and maintained in a database of the Department of State; and\n**(B)**\nto the extent practicable, provide for the sharing of such data with the Secretary of Commerce and the heads of such other Federal departments or agencies as the Secretary of State may determine relevant.\n##### (d) Effective date\nThis section shall take effect on the date that is 1 year after the date on which the Secretary of Commerce completes the transfer of the control over the export of previously covered items to the jurisdiction of the Department of State under section 3(a).\n#### 9. Limitation on licenses and other authorizations for export of certain items removed from the Commerce Control List and included on the United States Munitions List\n##### (a) In general\nThe Secretary of State may not grant a license or other authorization for the export of a previously covered item the control over the export of which the Secretary of Commerce has transferred to the jurisdiction of the Department of State under section 3(a) unless, before granting the license or other authorization, the Secretary submits to the chairman and ranking member of the Committee on Foreign Affairs of the House of Representatives and the chairman and ranking member of the Committee on Foreign Affairs of the Senate a written certification with respect to such proposed export license or other authorization containing\u2014\n**(1)**\nthe name of the person applying for the license or other authorization;\n**(2)**\nthe name of the person who is the proposed recipient of the export;\n**(3)**\nthe name of the country or international organization to which the export will be made;\n**(4)**\na description of the items proposed to be exported; and\n**(5)**\nthe value of the items proposed to be exported.\n##### (b) Form\nA certification required under subsection (a) shall be submitted in unclassified form, except that information regarding the dollar value and number of items proposed to be exported may be restricted from public disclosure if such disclosure would be detrimental to the security of the United States.\n##### (c) Deadlines\nA certification required under subsection (a) shall be submitted\u2014\n**(1)**\nat least 15 calendar days before a proposed export license or other authorization is granted in the case of a transfer of items to a country which is a member of the North Atlantic Treaty Organization or Australia, Japan, the Republic of Korea, Israel, or New Zealand, and\n**(2)**\nat least 30 calendar days before a proposed export license or other authorization is granted in the case of a transfer of items to any other country.\n##### (d) Congressional resolution of disapproval\nA proposed export license or other authorization described in paragraph (1) of subsection (c) shall become effective after the end of the 15-day period described in such paragraph, and a proposed export license or other authorization described in paragraph (2) of subsection (c) shall become effective after the end of the 30-day period specified in such paragraph, only if the Congress does not enact, within the applicable time period, a joint resolution prohibiting the export of the covered item for which the export license or other authorization was proposed.\n#### 10. Prohibition on promotion of covered munitions\nThe Secretary of Commerce is prohibited from\u2014\n**(1)**\npromoting the sale or export of covered munition; or\n**(2)**\nseeking the reduction or removal by any foreign country of restrictions on the marketing of covered munitions.\n#### 11. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Covered munition**\nThe term covered munition means the following:\n**(A)**\nAny previously covered item.\n**(B)**\nAny item that, following the date of the enactment of this Act, is designated for control under Category I, II, or III of the United States Munitions List pursuant to section 38 of the Arms Export Control Act ( 22 U.S.C. 2778 ) or otherwise subject to control under any such category.\n**(3) Previously covered item**\nThe term previously covered item means any item that\u2014\n**(A)**\nas of March 8, 2020, was included in Category I, II, or III of the United States Munitions List; and\n**(B)**\nas of the date of the enactment of this Act, is included on the Commerce Control List.\n**(4) Firearm**\nThe term firearm includes covered munitions.\n**(5) Gross violations of internationally recognized human rights**\nThe term gross violations of internationally recognized human rights has the meaning given that term in section 502B(d) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2304(d) ).\n**(6) Security assistance**\nThe term security assistance includes\u2014\n**(A)**\nthe types of assistance specified in section 502B(d)(2) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2304 ); and\n**(B)**\nassistance furnished under an international security assistance program of the United States conducted under any other provision of law, including under the authorities under chapter 16 of title 10, United States Code.\n**(7) United States Munitions List**\nThe term United States Munitions List means the list maintained pursuant to part 121 of title 22, Code of Federal Regulations.",
      "versionDate": "2025-12-16",
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
        "name": "International Affairs",
        "updateDate": "2026-01-08T16:44:12Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6736ih.xml"
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
      "title": "ARMAS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARMAS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Americas Regional Monitoring of Arms Sales Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the transfer of regulatory control of certain munitions exports from the Department of Commerce to the Department of State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:17Z"
    }
  ]
}
```
